# KiCad project

Open **pd-bench.kicad_pro** in KiCad 10.0.x. Revision 0.2 contains a fully routed PCB, checked with KiCad CLI 10.0.5. Keep this folder and its local libraries together.

```text
hardware/
  pd-bench.kicad_pro       Project settings and net classes
  pd-bench.kicad_sch       One-sheet A3 schematic (electrically unchanged)
  pd-bench.kicad_pcb       Routed 80 x 70 mm two-layer PCB
  pd-bench.kicad_dru       Documented J1-specific design rules
  sym-lib-table           Project-relative symbol library
  fp-lib-table            Project-relative footprint library
  libraries/
    PD_Bench.kicad_sym
    PD_Bench.pretty/
```

The PCB contains 27 schematic-linked footprints and four board-only mounting holes, 112 track segments, 48 vias and three filled copper zones. There are zero unconnected items under the supplied DRC. Four additional zones are mounting-hardware keepout areas, not copper pours.

Local symbols and footprints are derived from KiCad standard libraries. The MOSFET symbol represents G1/D2/S3. J3/J4 nominal drills have been changed to 1.1 mm in both board and local libraries. The USB footprint retains the manufacturer's land pattern and uses a documented 0.19 mm internal hole-clearance rule. Fabricator acceptance of its nominal 0.1944 mm spacing remains open.

Optional component 3D bodies reference KiCad's standard model library. The supplied bare-board CAD render intentionally does not establish an assembled hardware result. Use the copper exports and native PCB to inspect routing.

Before fabrication, review the [layout](../docs/pcb-layout.md), [routing assessment](../docs/routing-review.md) and [open issues](../docs/open-issues.md). This is an unbuilt design prototype; no manufacturing files are released.

Re-run from the repository root with `kicad-cli` on the path:

```sh
kicad-cli sch erc -o verification/erc.rpt hardware/pd-bench.kicad_sch
kicad-cli sch export netlist --format kicadxml -o verification/netlist.xml hardware/pd-bench.kicad_sch
kicad-cli pcb drc --refill-zones --save-board --schematic-parity --exit-code-violations -o verification/drc.rpt hardware/pd-bench.kicad_pcb
python verification/check_connectivity.py
```

The optional `verification/inspect_routed_board.py` uses KiCad's bundled Python/pcbnew module to compare every PCB pin with the exported schematic and report routing/zone statistics. File checks are not electrical simulation or physical validation.
