# Revision 0.2 routing review

**Routed design prototype | Unbuilt | 2026-09-06**

Routing closes the unfinished PCB work from revision 0.1. No circuit nets, component values or MPNs were changed. The schematic remains circuit revision 0.1; PCB/package revision 0.2 adds placement corrections, routing, ground stitching, a drain copper spreader and documented footprint rules.

## Verification scope

KiCad 10.0.5 reports **0 DRC violations, 0 unconnected items and 0 schematic parity issues** with filled zones and the included project settings. No DRC exclusions were added. The clean result includes the explicit J1 rules; it is not a pass against the original blanket hole-clearance constraint. Existing default ignored check categories are listed in the report.

The independent pin-map check compares the exported schematic's 89 pin assignments with the recorded design and verifies 17 critical polarity/control assignments. A native-board audit also compares every linked PCB pad net to the exported schematic, including the deliberately unconnected pins. Checks establish CAD consistency, not correct PD behavior or protection performance.

## Geometry and current path

- 31 footprints: 27 from the schematic and four M3 mounts.
- 112 track segments and 48 vias: four input-power vias, two gate-control vias, and 42 ground vias.
- Three filled copper pours: one front VOUT spreader and front/back ground. Each ground pour has one connected filled polygon.
- Main fused and output traces are 2.00 mm wide. USB fanout and device lands are narrower; their current density and temperature must be checked physically.
- Back copper is primarily ground. Its only non-ground routes are the short input contact link and two gate-control connections.
- Four mounting keepouts reserve a 7 mm diameter for screw heads/washers on both layers.

For a screening calculation, 35 um copper has approximately 0.493 mOhm per square at room temperature using rho=1.724e-8 ohm m. The approximately 16.7 mm fused trunk at 2 mm width contributes about 4.1 mOhm; the approximately 40.7 mm output route at 2 mm width gives about 10.0 mOhm before crediting the parallel VOUT pour. Together that is roughly 28 mV and 56 mW at 2 A. This omits input fanout, vias, return spreading, contacts, fuse and MOSFET. It is not a board-level voltage-drop or temperature prediction.

Assuming 25 um via-wall copper, a 1.6 mm long via with 0.4 mm finished hole has about 0.88 mOhm barrel resistance. Two parallel barrels are about 0.44 mOhm if current shares equally. Actual wall thickness and current sharing are fabricator/geometry dependent. Neither this estimate nor the nominal trace width qualifies the 2 A target.

## Documented special case

The [GCT USB4105 B4 drawing, sheet 1](https://gct.co/files/drawings/usb4105.pdf) specifies the tight connector land pattern. The retained local footprint has nominal 0.1944 mm copper-to-locator-hole clearance. The project uses 0.19 mm only between items belonging to J1; the general 0.25 mm drilled-hole rule remains in force elsewhere. J1 also uses 0.20 mm contact-fanout clearance and solid SMD ground connections. Fabricator review of locator-hole diameter, position tolerance and copper registration remains open (O02).

Wurth header drawings call for nominal 1.1 mm holes. J3/J4 board pads and local footprints now match that value, with 0.30 mm nominal annular rings. Procurement and finished-hole tolerance still require normal fabrication review.

## Evidence and remaining work

See the [DRC report](../verification/drc.rpt), [verification record](../verification/README.md), and front/back copper exports. The bare-board image is a CAD rendering, not a photograph, and does not depict an assembled or tested device. No Gerbers or drills are released. Fabrication review and all physical tests in the [validation plan](validation-plan.md) remain outstanding.
