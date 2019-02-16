#!/usr/bin/env python
#MenuTitle: Populate ranges
# -*- coding: utf-8 -*-
# 
# If you have one or more glyphs selected in given ranges, it will ensure that
# all the rest of the glyphs from those ranges are created. 
# 
# Note: it will default to setting the display name of newly created glyphs to
# the codepoint.  This can be easily remedied by running one of the "set display
# name scripts".
#
# If the script is invoked with no selection it will populate the default ranges
# that are uncommented below.
# 
# The script should be added to Glyphs scripts folder and expects the following
# SMuFL and Bravura metadata files to be present in the same directory.
# 
# - bravura_metadata.json
# - glyphnames.json
# - ranges.json
#
# Written by Ben Timms - Steinberg Media Technologies GmbH 2018
# Use, distribute and edit this script as you wish!
#
__doc__="""

"""

import sys
from smufl_glyphs import SMuFLFontSyncer, invoke_menu_item

# Uncomment any ranges that you'd like to be populated when nothing is selected.
DEFAULT_RANGES_TO_POPULATE = [
    # u'articulation',
    # u'articulationSupplement',
    # u'barlines',
    # u'barRepeats',
    # u'beamedGroupsOfNotes',
    # u'beamsAndSlurs',
    # u'chordSymbols',
    # u'clefs',
    # u'clefsSupplement',
    # u'commonOrnaments',
    # u'dynamics',
    # u'flags',
    # u'holdsAndPauses',
    # u'individualNotes',
    # u'lyrics',
    # u'miscellaneousSymbols',
    # u'multiSegmentLines',
    # u'noteheads',
    # u'noteNameNoteheads',
    # u'octaves',
    # u'octavesSupplement',
    # u'otherAccidentals',
    # u'otherBaroqueOrnaments',
    # u'precomposedTrillsAndMordents',
    # u'repeats',
    # u'rests',
    # u'roundAndSquareNoteheads',
    # u'shapeNoteNoteheads',
    # u'shapeNoteNoteheadsSupplement',
    # u'slashNoteheads',
    # u'staffBracketsAndDividers',
    # u'standardAccidentals12Edo',
    # u'standardAccidentalsChordSymbols',
    # u'staves',
    # u'stems',
    # u'stringTechniques',
    # u'timeSignatures',
    # u'timeSignaturesSupplement',
    # u'tremolos',
    # u'tuplets',
    # u'vocalTechniques',
]

currentFont = Glyphs.font

selected_glyphs = currentFont.selection
if len(selected_glyphs) == 0:    
    ranges_to_populate = DEFAULT_RANGES_TO_POPULATE
else:
    ranges_to_populate = []
    for g in selected_glyphs:
        range_id = g.userData['smufl_range']
        if range_id is not None and range_id not in ranges_to_populate:
            ranges_to_populate.append(range_id)            

if len(ranges_to_populate) == 0:
    print("No ranges to populate")
    sys.exit()

smufl_font_syncer = SMuFLFontSyncer(currentFont)
currentFont.disableUpdateInterface()
smufl_font_syncer.populate_ranges(ranges_to_populate)
currentFont.enableUpdateInterface()



