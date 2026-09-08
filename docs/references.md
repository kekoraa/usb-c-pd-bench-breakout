# Technical references

Circuit references reviewed on 2026-09-05; revision 0.2 routing and mechanical review on 2026-09-06. Manufacturer pages may update; recheck at procurement. No manufacturer qualification transfers automatically to this board.

| ID | Primary reference | Used for |
|---|---|---|
| S1 | [Hynetek HUSB238 product and option table](https://en.hynetek.com/2421.html) | _002DD variant, disabled SOP-prime emulation, next-PDO mismatch action |
| S2 | [Hynetek HUSB238 datasheet v2.0, manufacturer-authored copy hosted by Adafruit](https://cdn-learn.adafruit.com/assets/assets/000/125/150/original/husb238_datasheet_full.pdf) | Pin map, setting tables, gate drive, limits and operation, pp. 3-10 |
| S2a | [Hynetek datasheet v2.5 link](https://en.hynetek.com/uploadfiles/site/219/news/b038530d-67c0-4ba0-9269-de0e666cb35b.pdf) | Current version linked by manufacturer; file retrieval unavailable during review; compare before release |
| S3 | [TI TVS2200 datasheet, rev. C](https://www.ti.com/lit/ds/symlink/tvs2200.pdf) | Standoff/clamp ratings, pins and layout |
| S4 | [Diodes DMP4015SK3 datasheet](https://www.diodes.com/datasheet/download/DMP4015SK3.pdf) | P-channel device, gate/drain/source mapping, resistance and SOA |
| S5 | [Nexperia BZT52 series datasheet](https://assets.nexperia.com/documents/data-sheet/BZT52_SER.pdf) and [ordering table](https://www.nexperia.com/products/diodes/zener-diodes/series/BZT52-C-SERIES.html) | 12 V gate clamp and BZT52-C12X ordering code |
| S6 | [Littelfuse 451/453 datasheet](https://www.littelfuse.com/~/media/electronics/datasheets/fuses/littelfuse_fuse_451_453_datasheet.pdf.pdf) | Fuse cold resistance, voltage rating, curves and land pattern |
| S7 | [GCT USB4105 specification](https://gct.co/files/specs/usb4105-spec.pdf) | Receptacle family electrical specification |
| S8 | [Phoenix Contact 1715022](https://www.phoenixcontact.com/en-us/products/printed-circuit-board-terminal-mkds-15-2-1715022) | 5.00 mm terminal pitch and connection details |
| S9 | [Wurth 61301021121](https://www.we-online.com/components/products/datasheet/61301021121.pdf) | Selector header dimensions |
| S10 | [Wurth 61300211121](https://www.we-online.com/components/products/datasheet/61300211121.pdf) | Enable header dimensions and recommended drill |
| S11 | [Wurth 60900213421](https://www.we-online.com/components/products/datasheet/60900213421.pdf) | Shunt accessory |
| S12 | [Murata GRM31CR71H475KA12L](https://www.murata.com/en-eu/api/pdfdownloadapi?cate=luCeramicCapacitorsSMD&partno=GRM31CR71H475KA12L) | Input capacitor identity and ratings |

Additional references for later revisions: [TI INA226](https://www.ti.com/product/INA226), [ST STUSB4500](https://www.st.com/en/interfaces-and-transceivers/stusb4500.html), and [USB-IF document library](https://www.usb.org/documents). Formal USB compliance requirements and all passive supplier curves remain part of the pre-release review. No formal compliance analysis was performed here.

Routing references: [GCT USB4105 drawing B4, 2023-12-18, sheet 1](https://gct.co/files/drawings/usb4105.pdf), reviewed for connector edge datum, 0.65 mm locator holes and 0.60 x 1.15 mm ground lands; [KiCad 10 custom design rules](https://docs.kicad.org/10.0/en/pcbnew/pcbnew.html#custom_design_rules), used for scoped hole-clearance and zone-connection rules.
