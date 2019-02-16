For these scripts to work, you'll need to put three SMuFL metadata files into the same folder as the scripts: 

- bravura_metadata.json
- glyphnames.json
- ranges.json

**Important note: these scripts will modify your Glyphs project / font file so it's critical to have backups before running any operations.  While I've tested the scripts here, I cannot guarantee that it will work in every single situation.**

Now I've got the disclaimer out of the way, the first thing to run is the "Set metadata.." script.  You should see all your glyphs coloured and categorised.  If you then run the "Set Glyph names to SMuFL names" it should sort them into the categories.  You can switch between SMuFL names, descriptions and codepoints using these three scripts.  My understanding is that you should run the "Set Glyph names to codepoints" before doing a final export of your font file for maximum compatibility with various applications which expect the glyph names to correspond to the codepoint.

Once the metadata is set on the glyphs, the "generate_font_metadata.py" script should work as expected.

There's one more extra script which is called "Populate ranges".  If you select one or more glyphs and run this script, it will create any other missing glyphs from that range as empty glyphs.  You can also edit the script and uncomment or edit the DEFAULT_RANGES_TO_POPULATE array with the range you'd like to create.  Running the script with no glyphs selected will create the default ranges from this list.

