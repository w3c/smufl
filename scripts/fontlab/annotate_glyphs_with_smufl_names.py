#FLM: Annotate glyphs with SMuFL names
#
# This script will iterate over the glyphs in a font and set the "note" field to the
# SMuFL glyph name for that codepoint, based on data in the SMuFL glyphnames.json file.
#
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

GLYPHNAMES_JSON_FILEPATH = ''

if not os.path.exists(GLYPHNAMES_JSON_FILEPATH) or \
    os.path.basename(GLYPHNAMES_JSON_FILEPATH) != 'glyphnames.json':
    raise Exception("Please set the GLYPHNAMES_JSON_FILEPATH variable to the path to "\
                    "the glyphnames.json file from the SMuFL metadata bundle")

glyphnames_data = json.load(open(GLYPHNAMES_JSON_FILEPATH, 'r'))
glyphnames_for_codepoint = {}

# Build a map of glyph names indexed on codepoint
for glyphname, glyphdata in glyphnames_data.iteritems():
    glyphnames_for_codepoint[int(glyphdata['codepoint'][2:], 16)] = glyphname

def set_glyph_note_to_smufl_name(font, glyph, glyphindex):
    #print "Glyph name: %s note: %s: unicode: %s\t" % (glyph.name, glyph.note, glyph.unicode),
    for codepoint in glyph.unicodes:
       if codepoint in glyphnames_for_codepoint:
           print "Setting 'note' for codepoint %s to '%s'" % (hex(codepoint), glyphnames_for_codepoint[codepoint])
           glyph.note = str(glyphnames_for_codepoint[codepoint])
           return

    print "Unable to lookup SMuFL name for glyph %s" % glyph.name

for glyph in fl.font.glyphs:
    set_glyph_note_to_smufl_name(fl.font, glyph, glyph.index)

fl.UpdateFont()
