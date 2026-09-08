# Component selection

The [BOM](../bom/bom.csv) contains one row per reference plus the two shunt accessories. The three test points are etched PCB features. Four non-plated mounting holes are board geometry and have no purchased component. No prices or inventory are asserted.

| Function | Selected part | Reason / review point |
|---|---|---|
| PD sink | Hynetek HUSB238_002DD, DFN-10 + exposed ground pad | Resistor-selected operation; variant disables SOP-prime emulation. Confirm procurement suffix and factory options. [S1-S2](references.md) |
| VBUS clamp | TI TVS2200DRVR, WSON-6 | 22 V standoff; tighter clamping than a conventional 22 V SMA TVS. [S3](references.md) |
| Output switch | Diodes DMP4015SK3-13, TO-252 | 40 V P-channel MOSFET with low resistance at 4.5 V drive; large drain pad simplifies heat spreading. [S4](references.md) |
| Gate clamp | Nexperia BZT52-C12X, SOD-123 | 12 V nominal gate-source clamp; avoids exposing the gate oxide to the full transient voltage. [S5](references.md) |
| Fuse | Littelfuse 0451003.MRL | 3 A, 125 VDC one-time fuse; low cold resistance and a published time-current curve. [S6](references.md) |
| USB-C receptacle | GCT USB4105-GF-A | Established 16-contact USB2 footprint with mechanical shell stakes. Data contacts unused. [S7](references.md) |
| Output terminal | Phoenix Contact 1715022 | 2 positions, **5.00 mm** pitch; do not substitute a 5.08 mm part without changing footprint. [S8](references.md) |
| Selector / enable | Wurth 61301021121 / 61300211121 | Ordinary through-hole headers used only for configuration/gate current. [S9-S10](references.md) |
| Shunts | Wurth 60900213421 | Removable 2.54 mm shunts. [S11](references.md) |
| Input capacitor | Murata GRM31CR71H475KA12L | 4.7 uF, 50 V, X7R, 1206. [S12](references.md) |
| Controller / output capacitors | TDK C2012X7R1H105K125AB | 1 uF, 50 V, X7R, 0805; verify final supplier drawing and bias curve. [TDK](https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info?part_no=C2012X7R1H105K125AB) |
| LEDs | Lite-On LTST-C170KSKT / LTST-C170KGKT | Amber / green 0805 indicators; verify brightness at sub-mA current |
| Resistors | Yageo RC0805FR / RC1206FR series | 1% values; 1206 resistors used for LED and bleeder dissipation |

Baseline protection deliberately stays small. A resettable polyfuse was not selected because hold/trip current varies strongly with temperature and its resistance increases output droop. The one-time fuse needs replacement after opening and is a backup wiring/fault element.

An STUSB4500-based revision is an alternative when nonvolatile PDO configuration and a configuration workflow are desired; it adds setup work compared with the resistor-only approach. See [ST's product information](https://www.st.com/en/interfaces-and-transceivers/stusb4500.html).

For a later metered version, consider **INA226AIDGSR**, a 10 mOhm four-terminal shunt, a 3.3 V supply and an external host. At 2 A the shunt alone loses 20 mV and dissipates 40 mW. That version needs bus-common-mode/transient checks, address/pull-up design, calibration, and additional documentation; none is populated in revision 0.2. [TI INA226](https://www.ti.com/product/INA226)

Do not replace protection devices solely by matching standoff voltage or package size. Check clamp voltage, pulse rating, leakage, pinout, gate-drive conditions and lifecycle. Reconfirm all procurement codes and package drawings before ordering; this is a design BOM, not an approved purchasing list.
