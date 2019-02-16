#MenuTitle: Generate SMuFL metadata JSON (Anchors + BBoxes)
# -*- coding: utf-8 -*-
# SMuFL metadata generator for Glyohs
# The script should be added to Glyphs scripts folder
#
# By default it will output the metadata file onto the user's desktop, but this can be changed
# by adjusting the value of the OUTPUT_DIR variable.
#
# Features currently supported:
# - engraving defaults
# - bounding boxes
# - anchors
#
# Written by Ben Timms - Steinberg Media Technologies GmbH 2018
# Use, distribute and edit this script as you wish!

import json
import os
from time import gmtime, strftime

OUTPUT_DIR = os.path.join( os.path.expanduser("~"), "Desktop" )

currentFont = Glyphs.font

# The values in the dictionary below should be manually edited
font_metadata = {
    "fontName": currentFont.familyName,
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


metadata_filename = os.path.join(OUTPUT_DIR, "%s_metadata_%s.json" % ( currentFont.familyName,
                                                                       strftime( "%Y%m%d_%H%M%S", gmtime() ) ) )

print "Writing metadata to: %s" % metadata_filename

def to_cartesian(val):
    return float(val)/250
    
for g in currentFont.glyphs:
    if len(g.layers) != 1:
        print g, len(g.layers)

    layer = g.layers[0]

    glyph_name = g.userData['name']
    font_metadata["glyphBBoxes"][glyph_name] = \
        {"bBoxSW": [
            to_cartesian(layer.bounds.origin.x),
            to_cartesian(layer.bounds.origin.y)
        ],
            "bBoxNE": [
                to_cartesian(layer.bounds.origin.x + layer.bounds.size.width),
                to_cartesian(layer.bounds.origin.y + layer.bounds.size.height)
            ]
        }
    if len(layer.anchors) > 0:
        font_metadata['glyphsWithAnchors'][glyph_name] = {}

        for anchor in layer.anchors:
            font_metadata['glyphsWithAnchors'][glyph_name][anchor.name] = \
                [to_cartesian(anchor.position.x), to_cartesian(anchor.position.y)]
        
with open(metadata_filename, 'w') as outfile:
    json.dump(font_metadata, outfile, indent=True, sort_keys=True)

print "Done..."