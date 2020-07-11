#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.join(sys.path[0],".."))

from KicadModTree import *
from KicadModTree.nodes.specialized.PadArray import PadArray

def inch_to_mm(x):
	return x * 25.4;

def create_footprint(name, is_left):

	kicad_mod = Footprint(name)
	kicad_mod.setDescription("Pads to one side of Tektronix TM500/5000 " \
	"PCB edge connector")

	pitch = inch_to_mm(.156)
    	top = -(14 * pitch + pitch / 2)

	kicad_mod.append(Text(type='reference', \
		text = 'REF**', \
		at = [0, top - pitch], \
		layer = 'F.SilkS'))
    	kicad_mod.append(Text(type='value', \
		text = name, \
		at = [0, -top + pitch], 
		layer='F.Fab'))

	letter = 'A' if is_left else 'B'
    	for i in range(0, 28):
		x = inch_to_mm(0.12)
		y = top + i * pitch
		if is_left:
			x = -x
		pad_name = str(28 - i) + letter
		kicad_mod.append(Pad(number = 28 - i, \
		type = Pad.TYPE_THT, \
		shape = Pad.SHAPE_CIRCLE, \
		at = [0, y], \
		size = [inch_to_mm(.08), inch_to_mm(0.08)], \
		drill = inch_to_mm(0.032), \
		layers = ['*.Cu', '*.Mask']))
		kicad_mod.append(Text(type='user', 
		text = pad_name, 
			at = [x, y], 
			layer='F.SilkS'))

	file_handler = KicadFileHandler(kicad_mod)
	file_handler.writeFile(name + '.kicad_mod')
 
if __name__ == '__main__':

	create_footprint("left_tek_tm", True);
	create_footprint("right_tek_tm", False);
