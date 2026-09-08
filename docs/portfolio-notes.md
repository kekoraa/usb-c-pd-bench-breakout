# Portfolio and interview notes

## Honest project description

“Developed a design-stage USB-C PD bench breakout around an autonomous sink controller, with five voltage-request settings, a fuse, transient suppression, a controlled MOSFET output and rail indicators. Prepared a KiCad schematic, a routed two-layer PCB, a component BOM, loss and stress calculations, and a future validation plan. The prototype has not been built or physically tested.”

Use this wording only after reviewing the files and being able to explain the decisions. Keep the actual scope of your work clear. A design-stage project can demonstrate engineering judgment without claiming measured performance.

## Claims supported by this package

- Defined requirements and selected real parts against manufacturer documentation.
- Developed a schematic and checked its electrical consistency with KiCad ERC.
- Completed two-layer PCB routing, filled ground and output zones, and checked connectivity, schematic parity and documented design rules.
- Calculated preliminary loss, gate-drive, transient margin and output-discharge behavior.
- Identified limitations and planned validation with observable acceptance criteria.

## Claims not supported

“Built a 40 W bench supply,” “tested at 2 A,” “validated USB PD interoperability,” “manufacturing-ready,” “certified,” “short-circuit proof,” “reverse-polarity protected,” “high efficiency measured,” and “all five voltages guaranteed.” Do not convert targets into results or use a 3D CAD image as a hardware photograph.

## Interview discussion prompts

| Prompt | Point to explain |
|---|---|
| Why no converter? | The source changes VBUS after negotiation; the board mainly passes power through. |
| Why can 12 V fail to appear? | The source may not advertise it, or may not meet the request current. |
| Why 2.25 A request for a 2 A output? | It leaves overhead for the board itself; it still does not limit load current. |
| Why a 3 A fuse? | Continuous derating and fault-energy coordination; a fuse is not a programmable limiter. |
| Why clamp the MOSFET gate? | VGS must stay within its own rating, independent of the VDS rating. |
| What does the missing selector do? | It requests 20 V; assembly defaults and the separate enable control must address this explicitly. |
| What is the biggest next step? | Obtain fabrication/assembly review, then validate negotiation, inrush and temperature on hardware. |

Use the routed layout or block diagram as the repository image. Label PCB images “routed CAD design; unbuilt prototype.” Explain the USB footprint-specific clearance rule if discussing the clean DRC report. Replace design targets with measured results only after the corresponding tests are complete and recorded.
