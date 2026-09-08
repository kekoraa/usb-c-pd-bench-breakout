"""Audit the native PCB using KiCad's Python/pcbnew module; not a simulator.

Run from any directory with KiCad's bundled Python. DRC must also be run using
kicad-cli pcb drc --refill-zones --save-board --schematic-parity.
"""
from pathlib import Path
import collections
import hashlib
import json
import xml.etree.ElementTree as ET
import pcbnew as p

root = Path(__file__).resolve().parents[1]
board_path = root/'hardware/pd-bench.kicad_pcb'
board = p.LoadBoard(str(board_path))
expected = {}
for net in ET.parse(root/'verification/netlist.xml').findall('./nets/net'):
    for node in net.findall('node'):
        expected[node.get('ref'), node.get('pin')] = net.get('name')

observed = set()
errors = []
pad_count = 0
for fp in board.GetFootprints():
    if fp.GetAttributes() & p.FP_BOARD_ONLY:
        continue
    for pad in fp.Pads():
        if not pad.GetNumber():
            continue  # stencil-only apertures do not represent electrical pins
        key = fp.GetReference(), pad.GetNumber()
        observed.add(key)
        pad_count += 1
        if expected.get(key) != pad.GetNetname():
            errors.append(f'{key}: PCB {pad.GetNetname()} vs schematic {expected.get(key)}')
        if key[0] in ['J3', 'J4'] and abs(p.ToMM(pad.GetDrillSize().x)-1.1) > 1e-6:
            errors.append(f'{key}: header drill is not nominal 1.1 mm')
if observed != set(expected):
    errors.append(f'Pin set mismatch: missing={set(expected)-observed}, extra={observed-set(expected)}')

segments = []
vias = []
lengths = collections.defaultdict(float)
for item in board.GetTracks():
    if isinstance(item, p.PCB_VIA):
        vias.append(item)
    else:
        segments.append(item)
        lengths[item.GetNetname(), board.GetLayerName(item.GetLayer()), round(p.ToMM(item.GetWidth()),4)] += p.ToMM(item.GetLength())
if not segments:
    errors.append('Board has no routed segments')
allowed_back = {'/VBUS_RAW','/PD_GATE','/ENABLE_GATE','/GND'}
for t in segments:
    if t.GetLayer() == p.B_Cu and t.GetNetname() not in allowed_back:
        errors.append(f'Unexpected back-side net: {t.GetNetname()}')
via_nets = collections.Counter(v.GetNetname() for v in vias)
# These layer changes have explicit routing intent; a via that acquired a
# crossing net during editing must not silently become part of the design.
expected_signal_vias = {(69.0,80.5):'/PD_GATE',(90.0,64.0):'/ENABLE_GATE',
    (59.2,71.9):'/VBUS_RAW',(60.2,71.9):'/VBUS_RAW',
    (59.2,78.1):'/VBUS_RAW',(59.2,79.0):'/VBUS_RAW'}
for v in vias:
    pos = (round(p.ToMM(v.GetPosition().x),4),round(p.ToMM(v.GetPosition().y),4))
    if v.GetNetname() != expected_signal_vias.get(pos,'/GND'):
        errors.append(f'Via net differs from intended layer change at {pos}')
zones = []
for z in board.Zones():
    if z.GetIsRuleArea():
        continue
    polygons = z.GetFilledPolysList(z.GetLayer()).OutlineCount()
    zones.append({'net':z.GetNetname(),'layer':board.GetLayerName(z.GetLayer()),'filled_polygons':polygons})
    if polygons == 0:
        errors.append('Empty copper zone')
for layer in ['F.Cu','B.Cu']:
    if not any(z['net']=='/GND' and z['layer']==layer and z['filled_polygons']==1 for z in zones):
        errors.append(f'{layer} lacks the intended single connected filled ground polygon')
result = {'kicad_version':p.Version(),'pcb_sha256':hashlib.sha256(board_path.read_bytes()).hexdigest(),
    'linked_pin_assignments':len(observed),'physical_numbered_pads':pad_count,
    'footprints':len(list(board.GetFootprints())),'track_segments':len(segments),
    'vias':len(vias),'vias_by_net':dict(sorted(via_nets.items())),
    'copper_zones':zones,'mounting_keepouts':sum(z.GetIsRuleArea() for z in board.Zones()),
    'track_lengths_mm':[{'net':n,'layer':l,'width_mm':w,'length_mm':round(length,4)} for (n,l,w),length in sorted(lengths.items())],
    'errors':errors,'status':'PASS' if not errors else 'FAIL',
    'scope':'Native CAD consistency and routing structure only; run DRC separately. No physical validation.'}
print(json.dumps(result,indent=2))
raise SystemExit(bool(errors))
