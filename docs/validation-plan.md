# Future bring-up and validation plan

**All tests below are planned and have not been performed.** Record data in [test-log.csv](test-log.csv); do not prefill outcomes. Begin only after the schematic, routed PCB, footprints and assembly receive review.

## Equipment and setup

Use a current-limited bench supply for controlled low-voltage checks, a known USB-C PD source, an inline PD analyzer with source-capability decoding, two cable orientations, a DMM, a programmable electronic load rated at least 60 W, an oscilloscope, and temperature probes or a thermal camera. Use protected fixtures and a nonconductive surface. Ground-referenced scope clips connect only to board GND; use a differential probe for gate-source and other floating measurements.

For direct bench injection, leave the USB cable disconnected. Connect 5 V to VBUS_FUSED/GND through a fixture and start with a 50 mA limit. This bypasses USB negotiation and F1; it verifies only the injected section. Never back-power a USB source through this setup.

| ID | Procedure | Proposed acceptance criterion / recorded evidence |
|---|---|---|
| V01 | Unpowered microscope and polarity inspection | Correct parts, no bridges, U1/U2 ground pads soldered, Q1/D1/LED orientation confirmed |
| V02 | Check rail resistance and every power-path pin | No unexplained low-resistance short; record readings after caps settle; match schematic and polarity |
| V03 | 5 V / 50 mA limited injection, J4 open | No sustained limit event; provisional no-load input current below 15 mA; no heating; no claim of PD operation |
| V04 | Remove injection; J3=5 V, J4 open; attach PD source | Log source PDOs, selected request and contract; output settles below 1 V after 0.1 s with only local C3 fitted |
| V05 | Both USB-C plug orientations | Same successful contract behavior; log analyzer traces |
| V06 | Exercise all five selector rows with USB unplugged between changes | Actual contract follows the documented controller policy and advertised capabilities; verify source current >=2.25 A before full load |
| V07 | Test source without 12 V and source with an insufficient-current PDO | Record fallback voltage; do not mark failed merely because 12 V is unavailable; ensure documentation matches observed policy |
| V08 | Confirm unloaded voltage; then fit J4 without a load | Observe startup VOUT and VGS; gate remains within its rated envelope; no unexpected sustained oscillation; log initial 5 V and transition behavior |
| V09 | Load 0.1, 0.5, 1.0 and 2.0 A at each supported profile | No reset or repeated negotiation; board-only drop <=150 mV at 2 A is the initial target; report actual min/max voltage |
| V10 | 30-minute soak at 2 A, 5 V and 20 V, ambient 20-30 C | Initial goals: measured component surfaces below 70 C, connector rise below 20 C; estimate junction temperature using an appropriate thermal method |
| V11 | Remove J4 with a resistive load and then without a load | Confirm output decay; local 1 uF-only output below 1 V within 0.1 s; measure VGS turn-off and residual output |
| V12 | Controlled input disconnect / hard reset / reconnect, J4 fitted | Capture VBUS/VOUT; identify initial 5 V and any automatic return of output; no claim of fail-safe latching |
| V13 | Load steps at representative profiles | Capture voltage excursion and settling; no excursion outside the connected load's agreed operating limits; define those limits before the test |
| V14 | Capacitive load characterization, starting at 1 uF and increasing cautiously | Capture inrush and Q1 VDS/IDS; compare pulse energy and trajectory with MOSFET SOA; stop at reset, oscillation or excess temperature |
| V15 | Controlled output overload with a current-limited fixture | Determine whether source folds back, resets or fuse opens; no promise of a 2 A trip or a particular clearing time |
| V16 | Staged overvoltage and transient review/test | Use a purpose-built isolated fixture and agreed energy limits; capture voltage at U1, not just at the clamp; compare to datasheet limits |

Do not begin with an uncontrolled short at 20 V. Evaluate the source's fault behavior at low voltage/current first, then develop a bounded test with energy limits. The 3 A fuse may never open behind a 2.25 A-limited source. A passed overload observation with one source is not universal protection evidence.

Do not connect an external supply to VOUT for a reverse-blocking test: this design intentionally lacks that capability. For inductive or motor loads, add load-specific suppression and a revised test plan. System ESD, CC short-to-VBUS and formal USB compliance require appropriate equipment and are separate from basic bring-up.

## Evidence to retain

Record board revision, serial/sample ID, source model and advertised PDOs, cable details, instrument models, probe configuration, ambient conditions, shunt positions, current, voltage, temperatures, waveforms and pass/fail rationale. Save raw traces with the test ID. Publish failures and modifications as new revisions rather than overwriting original results. Do not use a simulation plot or a component datasheet curve as measured board evidence.
