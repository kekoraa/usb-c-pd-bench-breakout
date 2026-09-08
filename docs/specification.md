# Project specification

Revision 0.2 is an electrical design and fully routed two-layer PCB study for an unbuilt USB-C power breakout. The objective is an explainable junior EE portfolio project with manageable component count and an explicit path to physical validation.

| Requirement | Design target | Verification method |
|---|---|---|
| Source | USB-C to USB-C PD supply; fixed SPR PDOs | Source-capability capture and both cable orientations |
| Voltage requests | 5 / 9 / 12 / 15 / 20 V ceiling | PD analyzer plus DMM; no promise of exact selection on incompatible sources |
| Current | 2 A output target; 2.25 A request | Contract inspection, load sweep, thermal soak |
| Power | Up to 40 W nominal output target | 20 V compatible source, steady load test |
| Output | J2 pin 1 positive, pin 2 return | Continuity, polarity and loaded drop |
| User controls | J3 profile shunt; J4 enable shunt | Unpowered selection and open/closed enable tests |
| Status | Input and output voltage-present LEDs | Observe at 5 V and 20 V; no contract claim |
| Protection | Fuse, transient clamp, controller-driven disconnect, gate clamp | Staged transient/fault evaluation |
| Mechanics | 80 x 70 mm, 1.6 mm FR-4, two layers, 1 oz copper, four M3 holes | CAD drawing and fabricator review |
| Assembly | 0805/1206 passives; DFN/WSON controller and TVS | Stencil/reflow plan and solder inspection |
| Firmware | None | Schematic inspection |
| Environment | Initial qualification target: 20-30 C, still air, open board | Record ambient and temperatures |

Output voltage equals source VBUS minus cable, connector, fuse, MOSFET and copper losses. No local buck/boost stage corrects this drop. Source capability is a prerequisite, not a property of this board. A 20 V / 2 A charger PDO does not meet the programmed 2.25 A request.

The 2 A target applies only after a suitable contract is confirmed. Non-PD and default USB current modes are outside the full-load use case. A fuse does not enforce advertised Type-C current, and this circuit does not measure load current.

Excluded from revision 0.2: MCU, display, integrated ammeter, battery charging, reverse-feed operation, hot profile changes under load, PPS, EPR, and certification testing. Blank validation records remain blank until hardware exists.
