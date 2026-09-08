# PCB layout

Revision 0.2 is a **fully routed 80 x 70 mm two-layer PCB**. The saved layout has 112 track segments, 48 vias and three filled copper zones, with no unconnected items. It remains unbuilt and has no released manufacturing files.

## Stackup and implemented rules

| Feature | Implemented design |
|---|---|
| Stackup | Two-layer FR-4, 1.6 mm; 35 um / 1 oz copper assumed per side |
| CC and fine controller fanout | 0.20 mm traces; other control traces 0.25-0.30 mm |
| Main F1-to-Q1 and Q1-to-J2 conductors | 2.00 mm front traces; Q1 drain also has a broad VOUT pour |
| USB input fanout | 0.50 mm contact escapes, 1.00 mm top collection, 1.50 mm short back-side link |
| Low-current power branches | 0.30-0.60 mm; not intended to carry the external load |
| Ordinary copper clearance | 0.20 mm |
| Power net clearance | 0.25 mm, except 0.20 mm at J1 contact fanout |
| VOUT pour clearance | 0.50 mm |
| Signal vias | 0.60 mm diameter / 0.30 mm drill |
| USB power and most ground stitching vias | 0.80 mm diameter / 0.40 mm drill |
| Copper to board edge | 0.50 mm minimum |
| Ordinary drilled-hole clearance | 0.25 mm |
| J1 internal locator-hole clearance | 0.19 mm scoped rule; 0.1944 mm actual nominal minimum; fabrication acceptance pending |
| J3/J4 | 1.10 mm nominal drilled holes, 1.70 mm lands, 0.30 mm nominal annular ring |
| Mounting | Four 3.2 mm NPTH holes with 7 mm diameter copper/track/via keepouts |

Net-class track widths are routing defaults, not proof of current capacity. The narrow supply branches serve resistors, LEDs, capacitors and test pads. J2 is the load connector; TP1/TP2 are probe pads.

## Placement and copper decisions

J1 faces the left edge. Its reference point is at (52.5, 75) mm; the footprint's PCB-edge datum is 0.10 mm inside the actual x=50 mm edge. This gives connector-mouth overhang and keeps the shell copper more than 0.50 mm from the edge. Check actual cable-shell clearance at the mechanical review.

The USB VBUS contact pairs join through a short back-side link with two 0.4 mm drilled vias at each end. The fused main path and MOSFET-to-terminal path remain on top. C1 and the TVS branch are adjacent to the fuse output; U2 has four nearby ground vias and explicit exposed-pad/ground-pin connections. C2 sits next to U1's supply pin, and the gate pull-up/clamp are grouped beside Q1.

CC1/CC2 run on top with a short crossing over the input-collection link near the connector; beyond that fanout their back-side ground reference is continuous. They are PD communication lines, not a USB data differential pair, and are not length matched. The two gate-control routes use the back layer. The ground plane remains connected around their ends, with top ground copper and 42 ground stitching/return vias linking both sides. Inspect return current around these routes before any EMI qualification.

The front VOUT zone contacts the Q1 drain directly for current spreading. It is **not ground**. Both ground pours form one connected polygon each after fill. Solid USB ground-contact connections and explicit 0.50 mm ground escapes carry the return to the shell/plane. Through-hole ground connectors retain thermal reliefs. Exposed-pad vias sit outside paste apertures; do not specify open via-in-pad processing.

## Before fabrication

Review the USB-specific rule with the intended fabricator. It records the manufacturer land pattern; it is not an approval of drill/registration capability. Do not substitute a generic 0.25 mm rule and ignore the resulting findings, or describe the special rule as a fabrication qualification.

Review exact MPN footprints, stencil apertures, mounting hardware, mask bridges, board thickness tolerance and assembly access. The header land changes must be retained if footprints are updated from libraries. Add panel tooling/fiducials to the assembler's requirements. Refill zones and repeat DRC with schematic parity after any edit. Generate and independently inspect Gerbers and drills only after the release gates are closed. Validate temperature, voltage drop, inrush, PD behavior and protection on hardware.
