#FLM: Add Bravura Anchors
# -*- coding: utf-8 -*-
#
# Add Bravura's anchors to an existing font
#
# The script can be added to FontLab's Macro folder or cut and paste into the script editor window
#
# To use this script,a
#
# Note: the script will not create glyphs if they already exist
# Note: the path to the glyphnames.json SMuFL metadata file will should be set
# in the GLYPHNAMES_JSON_FILEPATH variable below.
#
# Written by Ben Timms - Steinberg Media Technologies GmbH 2015
# Use, distribute and edit this script as you wish!

import json
import os
from time import gmtime, strftime

if fl.font is None:
    raise Exception("Please open a font first")

BRAVURA_METADATA_JSON_FILEPATH = ''

def from_cartesian(val):
	return int(val*250)

if not os.path.exists(BRAVURA_METADATA_JSON_FILEPATH) or \
    os.path.basename(BRAVURA_METADATA_JSON_FILEPATH) != 'bravura_metadata.json':
    raise Exception("Please set the BRAVURA_METADATA_JSON_FILEPATH variable to the path to "\
                    "the bravura_metadata.json file from the Bravura metadata bundle")

bravura_metadata = json.load(open(BRAVURA_METADATA_JSON_FILEPATH, 'r'))

# Loop over each glyph in the existing font an build up a map of notes to glyph IDs
glyphIndexesForNotes = {}
for glyph in fl.font.glyphs:
	if glyph.note not in glyphIndexesForNotes:
		glyphIndexesForNotes[glyph.note] = glyph.index
	elif glyph.note is None:
		continue
	else:
		print "There are multiple glyphs with the note: %s" % glyph.note

for glyphname, anchors in bravura_metadata['glyphsWithAnchors'].iteritems():
	if glyphname not in glyphIndexesForNotes:
		print "Glyph with name %s doesn't exist in this font" % glyphname
		continue

	glyph = fl.font.glyphs[glyphIndexesForNotes[glyphname]]
	if len(glyph.anchors) > 0:
		print "Glyph %s already has anchors, skipping" % glyphname
		continue

	print "Creating anchors for glyph %s" % glyphname
	for anchorName, anchorPoints in anchors.iteritems():
		x = from_cartesian(anchorPoints[0])
		y = from_cartesian(anchorPoints[1])
		print "Creating Anchor %s (x: %d, y: %d)" % (anchorName, x, y)
		newAnchor = Anchor(str(anchorName), x, y)
		glyph.anchors.append(newAnchor)

fl.UpdateFont()
# 33239 is FontSortByUnicode
fl.CallCommand(33239)
print "Done..."
