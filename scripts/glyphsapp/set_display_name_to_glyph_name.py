#MenuTitle: Set Glyph names to SMuFL names
# -*- coding: utf-8 -*-
# 
# Set the display name of the selected glyphs to show the SMuFL glyph name.
#
# NOTE: this should be run before exporting for maximum compatibility with apps
# that expect the glyphs to be named according to their codepoint.
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
Set the display name of the glyph to the SMuFL name of the glyph
"""

from smufl_glyphs import set_display_name_to, invoke_menu_item, GLYPHS_EDIT_MENU_DESELECT_ALL_IDX

currentFont = Glyphs.font

selected_glyphs = currentFont.selection
if len(selected_glyphs) == 0:    
    glyphs_to_change = currentFont.glyphs
else:
    glyphs_to_change = selected_glyphs

currentFont.disableUpdateInterface()
set_display_name_to(glyphs_to_change, 'name')
currentFont.enableUpdateInterface()
if len(selected_glyphs) == 0:
    print ("Deselecting...")
    invoke_menu_item(Glyphs, EDIT_MENU, GLYPHS_EDIT_MENU_DESELECT_ALL_IDX)
