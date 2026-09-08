# Design report
**PD Bench | Revision 0.2 | Unbuilt design study**

## Engineering objective

Provide a compact interface between a commercial USB-C PD source and a passive experimental DC load. The useful engineering work is selecting a contract, preserving a low-resistance power path, managing voltage stress, and defining what must be tested. An autonomous controller keeps the project small enough to explain without a firmware subsystem.

The delivered schematic and fully routed two-layer PCB are editable KiCad documents. The layout has passed KiCad DRC and schematic parity under the included rules. The board has not been fabricated, assembled, powered or simulated. All numbers below are hand calculations or manufacturer limits, not measurements. The maximum power figure is a target envelope and does not establish thermal capability.

## Architecture decisions

The HUSB238_002DD was selected for resistor configuration and its documented option set. The chosen variant does not emulate an e-marker. There is no intended operation above 3 A and no need for cable-identity emulation. The design programs a **2.25 A request**, retaining 250 mA overhead above the 2 A output target for controller, indicators and tolerances. This also means a source that advertises only 2 A at a given voltage is unsuitable for that request.

Selection specifies a ceiling, not voltage conversion. Hynetek's policy and source capabilities can produce a lower compatible PDO. The 12 V row is useful with suitable sources but is not universal. Use the selector as a request label and the DMM as the output-voltage check. The [Hynetek product table and datasheet](references.md) define the relevant controller behavior and must be reconciled with the actual purchased suffix before assembly.

A screw terminal keeps the board mechanically simple. Banana sockets typically need more board area and mechanical support; short, appropriately rated leads can connect J2 to an external banana fixture later. The connector's component rating does not establish this board's current rating.

## Power budget and losses

Nominal output targets are 10, 18, 24, 30 and 40 W at 5, 9, 12, 15 and 20 V with 2 A load. Actual terminal power is lower because of series losses. At 20 V the controller request corresponds to 45 W of source capacity; that is not a claim of 45 W usable output.

Using the MOSFET's 15 mOhm maximum at -4.5 V gate drive and 25 C, its loss at 2 A is `I^2 R = 4 x 0.015 = 0.060 W`; drop is 30 mV. A preliminary 2x hot-resistance allowance gives 0.12 W and 60 mV. This is a planning allowance, not a guaranteed temperature curve. Gate drive must remain strong enough at minimum 5 V VBUS. [DMP4015SK3](https://www.diodes.com/datasheet/download/DMP4015SK3.pdf)

F1's published nominal cold resistance is 22.7 mOhm: at 2 A, drop is about 45 mV and heat about 91 mW. Cold resistance is not a worst-case hot limit. A 3 A fuse carries the target current with derating margin, but fault clearing requires sufficient energy; a current-limited charger may fold back without opening it. Review the fuse curve against the actual source and thermal environment. [Littelfuse 451/453](https://www.littelfuse.com/~/media/electronics/datasheets/fuses/littelfuse_fuse_451_453_datasheet.pdf.pdf)

As an illustrative conductor calculation, for a 30 mm long, 2 mm wide, 35 um copper trace, `R = rho L/(w t)` with `rho = 1.724e-8 ohm m` gives 7.39 mOhm at room temperature. A similar return doubles this to 14.8 mOhm, approximately 30 mV and 59 mW at 2 A. Copper resistance alone does not predict safe temperature; pads, necks, vias and copper spreading matter.

This illustrative estimate is not a resistance extraction from the final routed board. The estimated cold path contribution from those elements is about 105 mV at 2 A, excluding both connectors and the USB cable. Set a preliminary board-only measured drop target of **150 mV maximum at 2 A**, J1 VBUS to J2 positive with the return path included. This is an acceptance target to test, not a computed guarantee.

## Gate-drive check

With 100 kohm gate pull-up and 2.49 kohm series resistance, the estimated unclamped gate drive magnitude is approximately `VBUS x 100k/(100k + 2.49k + 300)` using a 300 ohm controller pull-down assumption. At 4.75 V this is about 4.62 V before path drop. After an estimated 45 mV fuse drop it is about 4.58 V, so the 4.5 V resistance specification has little low-end margin. Confirm at the actual minimum input and hot fuse resistance; use a larger margin device if needed.

At 20 V with an approximately 12 V clamp, R4 carries about 3.2 mA. At 28.4 V and an 11.4 V clamp estimate it carries 6.83 mA; with -1% R4 tolerance this becomes 6.90 mA, below the controller's 10 mA gate-sink limit. R4 dissipates approximately 117 mW during that assumed transient; a 1206, 0.25 W resistor is selected for margin. It is not rated for continuous overvoltage operation; check pulse-energy and temperature derating before release. D1's steady 20 V operation is only tens of milliwatts. Zener knee voltage, temperature and switching waveforms still require evaluation. [Nexperia BZT52 series](https://assets.nexperia.com/documents/data-sheet/BZT52_SER.pdf)

## Voltage-stress coordination

TVS2200's 22 V standoff is above the assumed 21 V upper steady level for a nominal 20 V source. Its stated maximum clamp is 28.4 V under the specified 40 A, 8/20 us test condition, leaving 1.6 V below U1's 30 V absolute maximum. This margin excludes PCB inductive overshoot. U1's operating limit is lower than its absolute maximum: a transient survival comparison does not establish normal operation at 28.4 V. [TI TVS2200](https://www.ti.com/lit/ds/symlink/tvs2200.pdf)

Use short clamp connections, 50 V bus capacitors and a 40 V MOSFET. A conventional 22 V TVS can clamp far above its standoff voltage and is not an automatic substitute. U1's controller-driven output disconnect addresses slower overvoltage behavior; the clamp addresses short pulses. Neither is a guaranteed response to arbitrary sustained source faults. The controller remains on the source side of Q1.

This revision relies on the controller's integrated CC tolerance and does not contain a separate system-level CC ESD/short-to-VBUS protector. A CC fault review remains open. Do not add a low-voltage shunt TVS on CC and assume it can survive sustained contact with 20 V VBUS. Complete port protection is a separate design decision and test obligation.

## LEDs, capacitance and output decay

Assuming a 2 V LED forward drop, each 6.8 kohm resistor passes approximately 0.44 mA at 5 V and 2.65 mA at 20 V. Resistor dissipation at 20 V is about 48 mW; 1206, 0.25 W parts leave comfortable steady-state margin. Brightness at 5 V still needs observation.

The direct input has 4.7 uF plus 1 uF nominal. At +10% tolerance this is 6.27 uF, leaving room below a 10 uF preliminary attach-capacitance design ceiling. The local 1 uF output cap adds another 1.1 uF at +10% if Q1 is already enabled. External load capacitance is excluded from that budget. DC bias reduces capacitance and cannot be relied on to fix uncontrolled load inrush. USB attach and reset behavior must be checked against the applicable specification and measured with the actual source.

For local C3=1 uF and R10=10 kohm, the nominal time constant is 10 ms. Decay from 20 V to 1 V is `RC ln(20)`, approximately 30 ms; at +10% C and +1% R it is about 33 ms. An external 100 uF load raises the nominal result to about 3.03 s. Always measure the actual residual output before changing connections.

Stored energy in 100 uF at 20 V is 20 mJ. A fast turn-on or short can stress Q1 despite its low steady-state loss; its continuous-current headline is not a safe-operating-area guarantee. Large capacitive loads and hot plugging are not qualified by this revision. Add a suitably rated slew-controlled eFuse before expanding that scope.

## Release assessment

This is a credible circuit design proposal with native CAD and documented limits. A successful ERC and matching pin nets support its internal consistency. Routing is complete. Fabricator acceptance of the USB land pattern, procurement footprint approval, transient behavior, source interoperability and thermal tests remain necessary. See [routed layout review](routing-review.md) for the actual geometry and check scope. The [open-issue register](open-issues.md) and [validation plan](validation-plan.md) define the next work; no fabrication-ready claim is made.
