# Schematic implementation plan

The native schematic is included in `hardware/pd-bench.kicad_sch`. Short labelled wires join circuits through identically named nets. Its exported netlist is the electrical connectivity record; labels are not merely annotations. The design has six functional regions on one A3 sheet.

## Input and clamp

J1's four VBUS pins join `VBUS_RAW`. F1 connects this to `VBUS_FUSED`. All four ground contacts and the shell stakes join GND. CC1 and CC2 remain separate and go to U1 pins 4 and 5. Do not add separate 5.1 kohm pull-downs: the sink controller provides the terminations.

U2 pins 4/5/6 join `VBUS_FUSED`; pins 1/2/3 and pad 7 join GND. Put the clamp immediately after the fuse with a short, broad return. C1 is across the fused bus. R1 feeds `VIN_CTRL`; C2 decouples this filtered rail beside U1. F1 must carry all output and controller current. Keep `VBUS_RAW` copper very short.

## Controller pin map

| U1 pin | Name | Connection |
|---|---|---|
| 1 | VIN | VIN_CTRL; 1 uF local capacitor to GND |
| 2 / 3 | D+ / D- | Explicit no-connect |
| 4 / 5 | CC1 / CC2 | Corresponding USB-C CC contacts |
| 6 / 7 | SDA / SCL | Explicit no-connect; standalone operation |
| 8 | VSET | J3 odd pins |
| 9 | ISET | R2, 13.7 kohm, to GND |
| 10 | GATE | PD_GATE, to J4 pin 2 |
| 11 | Exposed GND pad | Solid GND connection; not optional |

The pin map and setting values are based on Hynetek's [manufacturer-authored datasheet](references.md). D+/D-, SBU and I2C are unused on this revision. Use a real USB-C PD source; legacy charging detection is not an evaluated feature.

## Output control

Q1 source pin 3 joins `VBUS_FUSED`. Drain pin 2 and the large tab join `VOUT`. Gate pin 1 joins `MOS_GATE`. The body diode points from output toward input: it blocks forward source-to-output current when Q1 is off but permits reverse feed. Never reverse source and drain to try to solve this limitation.

R3, 100 kohm, pulls the gate to source. D1 cathode/pin 1 connects to source and anode/pin 2 to gate. R4, 2.49 kohm, connects MOS_GATE to J4 pin 1. Fitting J4 closes the control path to the controller's open-drain gate driver; removing it allows R3 to turn Q1 off. J4 does not carry the output's 2 A current.

J4 is not a verified-PDO interlock. A fitted shunt can permit initial 5 V, fallback output, or automatic restart after reconnection. Q1 only follows the controller's drive and protection behavior. R4 limits gate current but does not implement a specified output slew rate or precision inrush control.

J2 pin 1 connects to VOUT and pin 2 to GND. C3 and R10 connect across VOUT/GND. R10 discharges the local output capacitor after Q1 switches off; external capacitance increases the decay time.

## Selection and indications

J3 pins 1/3/5/7/9 share VSET. Pin 2 is GND. Pins 4/6/8 return through R5/R6/R7, respectively, to GND. Pin 10 is deliberately unconnected so row 9-10 stores the shunt while requesting 20 V. Fit row 1-2 at assembly. Never change profiles with a connected load or USB power present.

R8/D2 indicate the fused input; R9/D3 indicate the output. LED cathodes go to GND. TP1 is fused input, TP2 output, TP3 ground. Power flags on VIN_CTRL and GND tell ERC that these rails are externally supplied through passive elements; they are not physical parts and are not evidence of a real supply.
