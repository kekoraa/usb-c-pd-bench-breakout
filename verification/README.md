# Verification record

**PCB/package revision 0.2 | Design-stage, unbuilt prototype | 2026-09-06**

Checks used KiCad CLI 10.0.5. The electrical schematic is unchanged from circuit revision 0.1.

| Check | Result | Evidence |
|---|---|---|
| Native schematic and SVG export | Passed | [Schematic](../docs/images/pd-bench.svg) |
| Schematic ERC | **0 errors, 0 warnings** | [erc.rpt](erc.rpt) |
| Intended connections vs. exported netlist | **27 components, 89 pin assignments pass** | [Check script](check_connectivity.py), [netlist](netlist.xml) |
| Critical polarity/control checks | **17 invariants pass**, plus current-setting and parking-pin checks | [Connectivity output](connectivity-check.txt) |
| Native PCB pad-net audit | **All linked pad nets match the schematic** | [Board audit](routed-board-audit.json), [audit script](inspect_routed_board.py) |
| PCB to schematic parity | **0 issues** | [drc.rpt](drc.rpt) |
| PCB DRC under documented project rules | **0 violations; no added exclusions** | [drc.rpt](drc.rpt), [drc.json](drc.json), [rules](../hardware/pd-bench.kicad_dru) |
| Routing completeness | **0 unconnected items** | 112 track segments, 48 vias, 3 filled copper zones |
| Visual review | Front/back copper and bare-board CAD render inspected | [Images](../docs/images/) |
| Physical tests, simulation, thermal qualification, compliance | **Not performed** | [Future validation plan](../docs/validation-plan.md) |

The four original USB hole-clearance findings are addressed by a J1-only 0.19 mm design rule, based on the reviewed GCT land pattern (nominal 0.1944 mm actual). This is a documented rule change, not measured fabrication acceptance. O02 remains open until the intended fabricator approves the geometry and tolerances. The ordinary drilled-hole clearance remains 0.25 mm. J1 uses 0.20 mm contact clearance and solid SMD ground connections; see [routing review](../docs/routing-review.md).

Default ignored check categories remain listed in the reports. Power flags declare supply ownership to ERC; they do not prove that power is present. Re-run checks after any edit. Clean CAD checks do not establish function, temperature, protection effectiveness, manufacturability, or USB compliance.

The exported netlist source-path metadata is normalized to a repository-relative path for portability; electrical data is unchanged.
