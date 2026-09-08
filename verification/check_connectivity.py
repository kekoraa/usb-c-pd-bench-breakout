"""Check exported KiCad connectivity and critical design invariants; no simulation."""
from pathlib import Path
import json, xml.etree.ElementTree as ET

root = Path(__file__).resolve().parent
design = json.loads((root / 'design-connectivity.json').read_text())
xml = ET.parse(root / 'netlist.xml')
actual = {}
for net in xml.findall('./nets/net'):
    for node in net.findall('node'):
        actual[(node.get('ref'), node.get('pin'))] = net.get('name')
errors = []
pin_count = 0
for component in design['components']:
    for pin, expected in component['nets'].items():
        pin_count += 1
        key = (component['ref'], pin)
        got = actual.get(key)
        if expected is None:
            if got is not None and not got.startswith('unconnected-'):
                errors.append(f'{key}: intended NC, got {got}')
        elif got != '/' + expected:
            errors.append(f'{key}: expected /{expected}, got {got}')

# Critical pin polarity / isolation requirements, independent of the component list.
checks = {
    ('Q1', '1'): '/MOS_GATE', ('Q1', '2'): '/VOUT',
    ('Q1', '3'): '/VBUS_FUSED', ('D1', '1'): '/VBUS_FUSED',
    ('D1', '2'): '/MOS_GATE', ('U1', '11'): '/GND',
    ('U2', '7'): '/GND', ('J2', '1'): '/VOUT', ('J2', '2'): '/GND',
    ('J1', 'A5'): '/CC1', ('J1', 'B5'): '/CC2',
    ('R2', '1'): '/ISET', ('R2', '2'): '/GND',
    ('J3', '1'): '/VSET', ('J3', '2'): '/GND',
    ('J4', '1'): '/ENABLE_GATE', ('J4', '2'): '/PD_GATE',
}
for key, expected in checks.items():
    if actual.get(key) != expected:
        errors.append(f'Critical invariant {key}: {actual.get(key)} != {expected}')
values = {c.get('ref'): c.findtext('value') for c in xml.findall('./components/comp')}
if values.get('R2') != '13.7 kohm 1%':
    errors.append('R2 must encode the documented 2.25 A request')
if actual.get(('J3', '10'), '').startswith('unconnected-') is False:
    errors.append('20 V shunt parking pin must remain unconnected')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(design["components"])} components, {pin_count} pin assignments, '
      f'{len(checks)} critical pin-net invariants, current-setting value and 20 V parking pin.')
print('This verifies file consistency, not circuit performance or manufacturing readiness.')
