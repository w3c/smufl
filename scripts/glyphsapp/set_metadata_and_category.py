#!/usr/bin/env python
#MenuTitle: Set metadata on selected (or all) glyphs, including categorisation
# -*- coding: utf-8 -*-
# 
# Set the metadata for all the selected glyphs in the font.
# If the script is invoked with no selection it will apply to all glyphs.
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

from smufl_glyphs import SMuFLFontSyncer, invoke_menu_item, GLYPHS_EDIT_MENU_DESELECT_ALL_IDX

BRAVURA_METADATA_FILENAME = "bravura_metadata.json"
GLYPHNAMES_FILENAME = "glyphnames.json"
RANGES_FILENAME = "ranges.json"

currentFont = Glyphs.font

selected_glyphs = currentFont.selection
if len(selected_glyphs) == 0:    
    glyphs_to_change = currentFont.glyphs
else:
    glyphs_to_change = selected_glyphs

smufl_font_syncer = SMuFLFontSyncer(currentFont, BRAVURA_METADATA_FILENAME, GLYPHNAMES_FILENAME, RANGES_FILENAME)
currentFont.disableUpdateInterface()
smufl_font_syncer.sync_metadata(glyphs_to_change)
currentFont.enableUpdateInterface()
# If there weren't any glyphs selected when this script was invoked, make sure there aren't any afterwards.
if len(selected_glyphs) == 0:
    invoke_menu_item(Glyphs, EDIT_MENU, GLYPHS_EDIT_MENU_DESELECT_ALL_IDX)