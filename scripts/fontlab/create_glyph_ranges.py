#FLM: Create SMuFL ranges
# -*- coding: utf-8 -*-
#
# SMuFL glyph range creator
#
# The script can be added to FontLab's Macro folder or cut and paste into the script editor window
#
# To use this script, simply uncomment the ranges that you wish to create from the CODEPOINT_RANGES array
# below (the first entry is uncommented as an example)
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

GLYPHNAMES_JSON_FILEPATH = ''

CODEPOINT_RANGES = [
  ["Staff brackets and dividers","E000","E00F"],
  # ["Staves","E010","E02F"],
  # ["Barlines","E030","E03F"],
  # ["Repeats","E040","E04F"],
  # ["Clefs","E050","E07F"],
  # ["Time signatures","E080","E09F"],
  # ["Noteheads","E0A0","E0FF"],
  # ["Slash noteheads","E100","E10F"],
  # ["Round and square noteheads","E110","E11F"],
  # ["Note clusters","E120","E14F"],
  # ["Note name noteheads","E150","E1AF"],
  # ["Shape note noteheads","E1B0","E1CF"],
  # ["Individual notes","E1D0","E1EF"],
  # ["Beamed groups of notes","E1F0","E20F"],
  # ["Stems","E210","E21F"],
  # ["Tremolos","E220","E23F"],
  # ["Flags","E240","E25F"],
  # ["Standard accidentals (12-EDO)","E260","E26F"],
  # ["Gould arrow quartertone accidentals (24-EDO)","E270","E27F"],
  # ["Stein-Zimmermann accidentals (24-EDO)","E280","E28F"],
  # ["Extended Stein-Zimmermann accidentals","E290","E29F"],
  # ["Sims accidentals (72-EDO)","E2A0","E2AF"],
  # ["Johnston accidentals (just intonation)","E2B0","E2BF"],
  # ["Extended Helmholtz-Ellis accidentals (just intonation)","E2C0","E2FF"],
  # ["Spartan Sagittal single-shaft accidentals","E300","E30F"],
  # ["Spartan Sagittal multi-shaft accidentals","E310","E33F"],
  # ["Athenian Sagittal extension (medium precision) accidentals","E340","E36F"],
  # ["Trojan Sagittal extension (12-EDO relative) accidentals","E370","E38F"],
  # ["Promethean Sagittal extension (high precision) single-shaft accidentals","E390","E3AF"],
  # ["Promethean Sagittal extension (high precision) multi-shaft accidentals","E3B0","E3EF"],
  # ["Herculean Sagittal extension (very high precision) accidental diacritics","E3F0","E3FF"],
  # ["Olympian Sagittal extension (extreme precision) accidental diacritics","E400","E40F"],
  # ["Magrathean Sagittal extension (insane precision) accidental diacritics","E410","E41F"],
  # ["Wyschnegradsky accidentals (72-EDO)","E420","E43F"],
  # ["Arel-Ezgi-Uzdilek (AEU) accidentals","E440","E44F"],
  # ["Turkish folk music accidentals","E450","E45F"],
  # ["Persian accidentals","E460","E46F"],
  # ["Other accidentals","E470","E49F"],
  # ["Articulation","E4A0","E4BF"],
  # ["Holds and pauses","E4C0","E4DF"],
  # ["Rests","E4E0","E4FF"],
  # ["Bar repeats","E500","E50F"],
  # ["Octaves","E510","E51F"],
  # ["Dynamics","E520","E54F"],
  # ["Lyrics","E550","E55F"],
  # ["Common ornaments","E560","E56F"],
  # ["Other baroque ornaments","E570","E58F"],
  # ["Combining strokes for trills and mordents","E590","E5AF"],
  # ["Precomposed trills and mordents","E5B0","E5CF"],
  # ["Brass techniques","E5D0","E5EF"],
  # ["Wind techniques","E5F0","E60F"],
  # ["String techniques","E610","E62F"],
  # ["Plucked techniques","E630","E63F"],
  # ["Vocal techniques","E640","E64F"],
  # ["Keyboard techniques","E650","E67F"],
  # ["Harp techniques","E680","E69F"],
  # ["Tuned mallet percussion pictograms","E6A0","E6BF"],
  # ["Chimes pictograms","E6C0","E6CF"],
  # ["Drums pictograms","E6D0","E6EF"],
  # ["Wooden struck or scraped percussion pictograms","E6F0","E6FF"],
  # ["Metallic struck percussion pictograms","E700","E70F"],
  # ["Bells pictograms","E710","E71F"],
  # ["Cymbals pictograms","E720","E72F"],
  # ["Gongs pictograms","E730","E73F"],
  # ["Shakers or rattles pictograms","E740","E74F"],
  # ["Whistles and aerophones pictograms","E750","E75F"],
  # ["Miscellaneous percussion instrument pictograms","E760","E76F"],
  # ["Beaters pictograms","E770","E7EF"],
  # ["Percussion playing technique pictograms","E7F0","E80F"],
  # ["Handbells","E810","E82F"],
  # ["Guitar","E830","E84F"],
  # ["Chord diagrams","E850","E85F"],
  # ["Analytics","E860","E86F"],
  # ["Chord symbols","E870","E87F"],
  # ["Tuplets","E880","E88F"],
  # ["Conductor symbols","E890","E89F"],
  # ["Accordion","E8A0","E8DF"],
  # ["Beams and slurs","E8E0","E8EF"],
  # ["Medieval and Renaissance staves","E8F0","E8FF"],
  # ["Medieval and Renaissance clefs","E900","E90F"],
  # ["Medieval and Renaissance prolations","E910","E92F"],
  # ["Medieval and Renaissance noteheads and stems","E930","E94F"],
  # ["Medieval and Renaissance individual notes","E950","E96F"],
  # ["Medieval and Renaissance oblique forms","E970","E98F"],
  # ["Medieval and Renaissance plainchant single-note forms","E990","E9AF"],
  # ["Medieval and Renaissance plainchant multiple-note forms","E9B0","E9CF"],
  # ["Medieval and Renaissance plainchant articulations","E9D0","E9DF"],
  # ["Medieval and Renaissance accidentals","E9E0","E9EF"],
  # ["Medieval and Renaissance rests","E9F0","E9FF"],
  # ["Medieval and Renaissance miscellany","EA00","EA1F"],
  # ["Medieval and Renaissance symbols in CMN","EA20","EA2F"],
  # ["Daseian notation","EA30","EA4F"],
  # ["Figured bass","EA50","EA6F"],
  # ["Function theory symbols","EA70","EA9F"],
  # ["Multi-segment lines","EAA0","EB0F"],
  # ["Electronic music pictograms","EB10","EB5F"],
  # ["Arrows and arrowheads","EB60","EB8F"],
  # ["Combining staff positions","EB90","EB9F"],
  # ["Renaissance lute tablature","EBA0","EBBF"],
  # ["French and English Renaissance lute tablature","EBC0","EBDF"],
  # ["Italian and Spanish Renaissance lute tablature","EBE0","EBFF"],
  # ["German Renaissance lute tablature","EC00","EC2F"],
  # ["Kievan square notation","EC30","EC3F"],
  # ["Kodály hand signs","EC40","EC4F"],
  # ["Simplified Music Notation","EC50","EC5F"],
  # ["Miscellaneous symbols","EC60","EC7F"],
  # ["Time signatures supplement","EC80","EC8F"],
  # ["Octaves supplement","EC90","EC9F"]
]

def format_codepoint(value):
    if (value > 0x10000):
        return "u"+hex(value).upper()[2:]
    else:
        return "uni"+hex(value).upper()[2:]


if not os.path.exists(GLYPHNAMES_JSON_FILEPATH) or \
    os.path.basename(GLYPHNAMES_JSON_FILEPATH) != 'glyphnames.json':
    raise Exception("Please set the GLYPHNAMES_JSON_FILEPATH variable to the path to "\
                    "the glyphnames.json file from the SMuFL metadata bundle")

glyphnames_data = json.load(open(GLYPHNAMES_JSON_FILEPATH, 'r'))
glyphnames_for_codepoint = {}

# Build a map of glyph names indexed on codepoint
for glyphname, glyphdata in glyphnames_data.iteritems():
    glyphnames_for_codepoint[int(glyphdata['codepoint'][2:], 16)] = glyphname

for codepoint_range in CODEPOINT_RANGES:
    range_name, range_start, range_end = codepoint_range

    for codepoint in range(int(range_start,16), int(range_end,16)):
        if codepoint not in glyphnames_for_codepoint:
            # This is an unused codepoint in the range
            continue
            
        hex_codepoint = hex(codepoint).upper()[2:]
        glyph_name = glyphnames_for_codepoint[codepoint]

        # Check for an existing glyph with this name
        gIndex = fl.font.FindGlyph(format_codepoint(codepoint))
        if gIndex > 0:
            # This glyph already exists
            print "%s (%s) already exists" % (glyph_name, hex_codepoint)
            continue

        print "Creating glyph %s at codepoint %s" % (glyph_name, hex_codepoint)
        g = Glyph()
        g.unicode = codepoint
        g.name = format_codepoint(codepoint)
        g.note = str(glyph_name)
        fl.font.glyphs.append(g)

fl.UpdateFont()
# 33239 is FontSortByUnicode
fl.CallCommand(33239)
