# Open issues and release gates

| ID | Issue | Closure evidence |
|---|---|---|
| O01 | **Closed in 0.2:** routing completed | 112 segments, 48 vias, 3 filled zones; DRC and schematic parity both zero |
| O02 | **Partially resolved:** GCT pattern reviewed; fabricator acceptance still open | 0.1944 mm nominal spacing retained with a J1-only 0.19 mm rule; obtain acceptance of hole size/location tolerances before fabrication |
| O03 | **Closed at design stage:** J3/J4 changed to nominal 1.1 mm drill | Board and local library match Wurth recommended nominal drill; 1.7 mm pads give 0.30 mm nominal annular ring |
| O04 | HUSB238 factory options and newer datasheet revision | Compare purchased _002DD against manufacturer v2.5 and reviewed v2.0 functional data; confirm power-on GATE, current setting and fallback |
| O05 | No physical performance evidence | Completed bring-up log, waveforms and thermal measurements |
| O06 | Small nominal transient headroom at U1 | Layout review and voltage capture at controller pins under defined pulse conditions |
| O07 | No precision current limiting or reverse blocking | Keep scope unchanged; redesign protection if scope expands |
| O08 | Gate resistor is not a specified inrush controller | Characterize local/startup capacitance and MOSFET SOA; add slew-controlled protection for larger loads |
| O09 | Missing selector shunt requests 20 V | Maintain default 5 V assembly shunt, clear markings and power-off selection procedure; evaluate a safer selector in a later revision |
| O10 | No external system-level CC protection | Complete CC fault/ESD review; select a compatible protector if required |
| O11 | Source-dependent fuse clearing | Match fuse time-current and pulse energy to source fault behavior and wiring |
| O12 | BOM lifecycle, passive ratings and footprints not procurement-approved | Recheck exact MPNs, package drawings, voltage-bias curves and assembler capabilities before purchasing |
| O13 | Public reuse license for original files not selected | Repository owner chooses a license while retaining third-party notices |

This register separates a completed design package from an approved manufacturing release. Do not close an issue merely because an ERC/DRC category is suppressed.
