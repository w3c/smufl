#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The script should be added to Glyphs scripts folder and is used by other scripts
#
# Written by Ben Timms - Steinberg Media Technologies GmbH 2018
# 
# Use, distribute and edit this script as you wish!
# -*- coding: utf-8 -*-
__doc__="""

"""

import json
import pprint
import binascii

if __name__ != '__main__':
	from __main__ import *
    
GLYPHS_NUMBER_OF_AVAILABLE_COLOURS = 12

GLYPHS_EDIT_MENU_SELECT_ALL_IDX   = 8
GLYPHS_EDIT_MENU_DESELECT_ALL_IDX = 9

def invoke_menu_item(glyphs_app, glyphs_menu, menu_index):
    glyphs_app.menu[glyphs_menu].submenu().performActionForItemAtIndex_(menu_index)

def formatUniGlyphName(codepoint):
    uniGlyphName = "uni%s" % codepoint.upper()
    # print(uniGlyphName)
    return uniGlyphName

def get_colour_for_category(category):
    return abs(hash(category)) % GLYPHS_NUMBER_OF_AVAILABLE_COLOURS

def from_cartesian(value):
    return value * 250

def set_display_name_to(glyphs_to_change, display_name_key):
    for glyph in glyphs_to_change:
        # print (glyph)
        availableUserData = glyph.userData.keys()
        if availableUserData is not None and display_name_key in availableUserData:
            glyph_display_name = glyph.userData[display_name_key]
            try:
                glyph.name = glyph_display_name
            except NameError:
                # NOTE: This only handles one clash - we would need recursion to 
                # handle multiple
                alt_glyph_display_name = "%s (1)" % glyph_display_name
                print("WARNING: Unable to set the glyph display name: %s as it already exists - falling back to %s" % (glyph_display_name, alt_glyph_display_name))
                glyph.name = alt_glyph_display_name
        else: 
            print ("WARNING: Display name key %s is not in glyph %s (Available keys: %s)" % (display_name_key, glyph, availableUserData))

class SMuFLFontSyncer(object):

    glyph_data_by_codepoint = {}

    def __init__(self, glyphs_font,
            bravura_metadata_filename="bravura_metadata.json",
            glyphnames_filename="glyphnames.json",
            ranges_filename="ranges.json"):
        self.font = glyphs_font
        with open(bravura_metadata_filename, "r") as bravura_metadata_fh:
            self.bravura_metadata = json.load(bravura_metadata_fh)
        with open(glyphnames_filename, "r") as glyphnames_fh:
            self.glyphnames = json.load(glyphnames_fh)
        with open(ranges_filename, "r") as ranges_fh:
            self.ranges_data = json.load(ranges_fh)

        self._populate_glyph_data_by_codepoint()

    def _populate_glyph_data_by_codepoint(self):
        """ Create a local cache of glyph and range data indexed by codepoint """
        for smufl_glyph_name, glyph_data in self.glyphnames.items():
            self.glyph_data_by_codepoint[glyph_data['codepoint'][2:]] = {
                'description': glyph_data['description'],
                'name': smufl_glyph_name}
        # Get the range and merge that in.
        for range_id, range_data in self.ranges_data.items():
            for glyphname_in_range in range_data['glyphs']:
                codepoint = self.glyphnames[glyphname_in_range]['codepoint'][2:]
                self.glyph_data_by_codepoint[codepoint]['range_id'] = range_id 
                self.glyph_data_by_codepoint[codepoint]['range_description'] = range_data['description'] 

    def sync_metadata(self, glyphs):
        """ Iterate over the provided glyphs, ensuring the metadata is set """
        for g in glyphs:
            if g.unicode not in self.glyph_data_by_codepoint:
                print ("WARNING: No metadata for %s" % g.unicode)
                continue

            glyph_data = self.glyph_data_by_codepoint[g.unicode]
            glyph_data['codepoint'] = g.unicode
            self._set_glyph_metadata(g, glyph_data )

    def _set_glyph_metadata(self, glyph, glyph_data):
        """ An internal method to set the metadata on the supplied glyph """
        glyph.storeCategory            = True
        glyph.category                 = glyph_data['range_description']
        glyph.color                    = get_colour_for_category(glyph_data['range_description'])
        glyph.unicode                  = glyph_data['codepoint']
        glyph.userData['description']  = glyph_data['description']
        glyph.userData['name']         = glyph_data['name']
        glyph.userData['uniCodepoint'] = formatUniGlyphName(glyph.unicode)
        glyph.userData['codepoint']    = glyph.unicode
        glyph.userData['smufl_range']  = glyph_data['range_id']
        return glyph

    def populate_ranges(self, ranges_to_populate):
        # print("Populating ranges: %s" % ranges_to_populate)
        for range_id in ranges_to_populate:
            self._populate_range(range_id)

    def _populate_range(self, range_id):
        print("Populating range: %s" % range_id)
        range_data = self.ranges_data[range_id]

        for smufl_glyph_name in range_data['glyphs']:
            codepoint         = self.glyphnames[smufl_glyph_name]['codepoint'][2:]
            # print ("SMuFL Glyph name %s - Codepoint: %s" % (smufl_glyph_name, codepoint))
            glyph             = self._get_or_create_glyph(codepoint)
            glyph_description = self.glyphnames[smufl_glyph_name]['description']
            glyph_data = {
                'name': smufl_glyph_name,
                'codepoint': codepoint,
                'description': glyph_description,
                'range_id': range_id,
                'range_description': range_data['description'],
            }
            self._set_glyph_metadata(glyph, glyph_data)
            # print ("Glyph: %s" % (glyph))
            # print ("Unicode: %s" % (glyph.unicode))

    def _get_or_create_glyph(self, codepoint):
        # Look for an existing glyph
        glyph = self.font.glyphs[codepoint]

        if glyph is None:
            glyph = GSGlyph(codepoint)
            self.font.glyphs.append(glyph)
        return glyph

 