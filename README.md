# tek_tm_ext
Tektronix TM500/TM5000 extender

Copyright (C) 2020 Lin Ke-Fong (anotherlin@gmail.com)\
*This project is free, you can do whatever you want with it.*

## Purpose

This is a small Kicad project for a Tektronix TM500/TM5000 extender. For calibration or repair, it 
is convenient to be able to work on the plug-ins outside of a mainframe. In addition, the 
designed PCB can be fitted with extra connectors and circuitry to allow standalone operation. That 
is, to allow plug-ins to be powered by lab supplies, hence providing a kind of controlled 
environment handy for debugging/repair.

## Prerequisites

This is a somewhat "low-level" project so it is expected that you already have some knowledge 
about the Tektronix TM500 and TM5000 systems, and electronics in general. The TM502A instruction 
manual (can be downloaded from TekWiki) is a very good summary, see page 6-3 in particular for a 
description of the TM500 plug-in interface. Refer to page 5-11 of the TM5006 instruction manual 
for a description of the TM5000 interface, which is basically the same, except for higher 
powered regulated DC supplies versus just filtered, and an additional PWR "power good" signal 
(some TM5000 plug-ins just ignore it). GPIB is a separate connector.

## How to make the PCB

The simplest is to use the generated gerber files ([gerber/tek_tm_ext-gerber-jlcpcb.zip](
./gerber/tek_tm_ext-gerber-jlcpcb.zip)), it should work with any PCB fab. They have been tested 
successfully at [JLCPCB](http://www.jlcpcb.com): Be sure to select "gold fingers" and "45 degrees" 
chamfered fingers, this is needed for the edge connector. It should cost you around 25 euros 
shipping included for 5 PCBs. If you used another PCB fab and the gerbers needed modification, 
please upload them on this repository so everybody can benefit.

The complete Kicad project is available [kicad/tek_tm_ext.zip](./kicad/tek_tm_ext.zip). You will 
need [pointhi/kicad-footprint-generator](http://github.com/pointhi/kicad-footprint-generator) for 
running the Python footprint generation script (code is a bit ugly, I'm a Python noob, sorry).

## Assembly

Please first have a look at the schematic ([tek_tm_ext.pdf](./tek_tm_ext.pdf)) and *BOM/parts 
needed* section at the end of this document.

Pins/pads are numbered from bottom to top. Looking from the front to the back of the TM500 or 
TM5000 mainframe, left is 'A' and right is 'B'. Solder wires between the PCB and the 56 pins 
connectors. For basic functionality, only pins A1 to A13 and B1 to B13 need to be soldered.
Depending on the plug-in at hand, supplemental pins may be soldered for extra connectivity 
functionalities. Use 22AWG or 24AWG wires. If available, .156" pitch (3.96mm) ribbon cable 
will make soldering easier.

Make sure to insert the polarizing key between pins 6 and 7, this is to ensure the 56 pins 
connector and the plug-in's PCB edge align correctly. You can do without but extra care will 
have to be taken during insertion.

If you intend to use the extender as a standalone debugging tool, fit the additional Molex 
connectors and (only needed for TM5000 plug-ins) the "power good" circuitry. The PCB is 
designed for .1" pitch (2.54mm) PCB header, so you may use any connector that fits. You
will have to prepare the cabling for connecting with the lab supplies and the pass transistors,
which have to be heatsinked.

It is recommended that you build 2 sets of extenders as some plug-ins make use of 2 
connections.

## Operation

* For use as a "simple" extender, just plug and play! If the "power good" circuitry has been 
fitted, then make sure to set the J11 jumper at 2-3 or leave it unconnected. 

* As a standalone debugging device, first check the service manual of the plug-in and find 
out what power supplies are needed. For DC voltages, use -26VDC, 26VDC, and 8VDC, this is what 
supplies a TM5000 mainframe. Set the current limits as low as permitted. For 25VAC, a 24VAC wall 
wart should be within tolerance. For 17.5VAC, two 9VAC wall warts can be connected to act as a 
center taped 18VAC transformer. In both cases, make sure the wall warts have the appropriate 
power rating(s). For TM5000 plug-ins, enable the "power good" signal by setting the J11 jumper
at 1-2. 

## BOM/parts needed

For wiring, use 22AWG or 24AWG (for example, Alpha Wire 1550 or 1551). If available, .156" pitch 
(3.96mm) ribbon cable will make assembly easier. The proposed pass transistors have appropriate 
specification for "high power" plug-ins (PS503 for example). The 56 pins connector is the same 
as JAMMA arcade so you can find cheaper alternatives than EDAC. In fact, all parts of the BOM 
may be substituted by appropriate generics.

| Symbol(s) | Name & Description | Part number | Quantity |
| --- | --- | --- | --- |
| J1 | 56 pins .156" (3.96mm) pitch edge connector | EDAC 307-056-500-202 | 1 |
| | Polarizing key, insert betwen pins 6 and 7 | EDAC 306-240-318 | 1 |
| | **_Parts below needed only for standalone debugging_** | | | |
| J3, J4, J9, J10 | PCB header, 2.54mm pitch, 3 circuits | Molex 22-23-2031 | 4 | 
| | Crimp housing, 2.54mm pitch, 3 circuits | Molex 22-01-3037 | 4 | 
| J4, J5, J8 | Vertical PCB header, 2.54mm pitch, 2 circuits | Molex 22-23-2021 | 3 |
| | Crimp housing, 2.54mm pitch, 2 circuits | Molex 22-01-3027 | 3 |
| | NPN pass transistor | TIP35C | 1 | 
| | PNP pass transistor | TIP36C | 1 |
| | Heat sink for TO-220/247 transistor | Ohmite FA-T220-38E | 2 |
| | **_Needed only for TM5000 plug-ins support_** | | | |
| R1 | 2.2K, 5%, 1/4W resistor | | 1 | 
| R2 | 4.7K, 5%, 1/4W resistor | | 1 |
| R3 | 200R, 5%, 1/4W resistor | | 1 | 
| R4 | 10K, 5%, 1/4W resistor | | 1 |
| Q1 | 2N3904 NPN transistor | | 1 |
| J11 | Pin header, 2.54mm pitch, 3 circuits | Harwin M20-9992046 (cut as needed) | 1 |
| | Jumper socket, 2 pins |  | 1 |

## Revision history and status

* **_Version 1.0_** Tested as working, both as extender and standalone. However, standalone AC supplies 
have not been tested, but confidence is pretty good that it works. The "power good" circuitry 
isn't tested, my AA5001 just ignores it.

* **_Version 0.8_** Needs a bodge wire to work.

## Acknowledgements

* Jerry Scheltgen and Dennis Tillman for their document (available at TekScope group) listing the
pass transistors used in the TM500 and TM5000 mainframes. This helped in the selection of the 
TIP35C and TIP36C.
