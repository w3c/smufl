#FLM: Generate SMuFL metadata JSON (Anchors + BBoxes)
# -*- coding: utf-8 -*-
#
# SMuFL metadata generator for FontLab
# The script can be added to FontLab's Macro folder or cut and paste into the script editor window
#
# By default it will output the metadata file onto the user's desktop, but this can be changed
# by adjusting the value of the OUTPUT_DIR variable.
#
# Features currently supported:
# - engraving defaults
# - bounding boxes
# - anchors
#
# Written by Ben Timms - Steinberg Media Technologies GmbH 2015
# Use, distribute and edit this script as you wish!

import json
import os
from time import gmtime, strftime

OUTPUT_DIR = os.path.join( os.path.expanduser("~"), "Desktop" )

if fl.font is None:
    raise Exception("Please open a font first")

# The values in the dictionary below should be manually edited
font_metadata = {
    "fontName": fl.font.font_name,
    "fontVersion": 1.12,
    "engravingDefaults": {
        "arrowShaftThickness": 0.16,
        "barlineSeparation": 0.4,
        "beamSpacing": 0.25,
        "beamThickness": 0.5,
        "bracketThickness": 0.5,
        "dashedBarlineDashLength": 0.5,
        "dashedBarlineGapLength": 0.25,
        "dashedBarlineThickness": 0.16,
        "hairpinThickness": 0.16,
        "legerLineExtension": 0.4,
        "legerLineThickness": 0.16,
        "lyricLineThickness": 0.16,
        "octaveLineThickness": 0.16,
        "pedalLineThickness": 0.16,
        "repeatBarlineDotSeparation": 0.16,
        "repeatEndingLineThickness": 0.16,
        "slurEndpointThickness": 0.1,
        "slurMidpointThickness": 0.22,
        "staffLineThickness": 0.13,
        "stemThickness": 0.12,
        "subBracketThickness": 0.16,
        "textEnclosureThickness": 0.16,
        "thickBarlineThickness": 0.5,
        "thinBarlineThickness": 0.16,
        "tieEndpointThickness": 0.1,
        "tieMidpointThickness": 0.22,
        "tupletBracketThickness": 0.16
    },
    "glyphsWithAnchors": {},
    "glyphBBoxes": {},
    "optionalGlyphs": {}}


metadata_filename = os.path.join(OUTPUT_DIR, "%s_metadata_%s.json" % ( fl.font.font_name,
                                                                       strftime( "%Y%m%d_%H%M%S", gmtime() ) ) )

print "Writing metadata to: %s" % metadata_filename

def to_cartesian(val):
    return float(val)/250
    
def format_codepoint(val):
    return hex(val).upper()[2:]

glyphs_with_anchors = {}
for g in fl.font.glyphs:
    if g.note is None or len(g.note) == 0:
        print "Skipping glyph with empty note (%s)"%g.name
        continue
    if g.nodes_number == 0 and len(g.components) == 0:
        print "Skipping glyph with no nodes (%s)"%g.name
        continue
    bounding_box = g.GetBoundingRect()

    font_metadata["glyphBBoxes"][g.note] = \
        {"bBoxSW": [
                    to_cartesian(bounding_box.ll.x),
                    to_cartesian(bounding_box.ll.y)
                    ],
         "bBoxNE": [
                    to_cartesian(bounding_box.ur.x),
                    to_cartesian(bounding_box.ur.y)
                  ]
        }

    if len(g.anchors) > 0:
        font_metadata['glyphsWithAnchors'][g.note] = {}
        for anchor in g.anchors:
            font_metadata['glyphsWithAnchors'][g.note][anchor.name] = \
                [to_cartesian(anchor.x), to_cartesian(anchor.y)]

    if int(g.unicode) >= 0xF400:
        font_metadata["optionalGlyphs"][g.note] = {'classes': []}
        font_metadata["optionalGlyphs"][g.note]['codepoint'] = "U+%s" % format_codepoint(g.unicode)

with open(metadata_filename, 'w') as outfile:
    json.dump(font_metadata, outfile, indent=True, sort_keys=True)

print "Done..."