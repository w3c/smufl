# FontLab scripts
To help in the preparation of SMuFL-compliant fonts and their associated metadata, a small collection of Python scripts for [FontLab Studio](http://www.fontlab.com/font-editor/fontlab-studio/) are available here.

## Running a script
To run a Python script from within FontLab Studio, refer to **Chapter 12: Macro Programming** of the [FontLab Studio 5 documentation](http://www.fontlab.com/font-editor/fontlab-studio/download-fontlab-studio/) for detailed instructions.

Assuming Python is correctly installed and detected by your installation of FontLab Studio, the following basic instructions should get you started:

* Show the Macro toolbar by choosing **View** ▸ **Toolbars** ▸ **Macro**
* Click the **Edit Macro** button in the Macro toolbar to show the **Edit Macro** window
* From the menu button in the **Edit Macro** window's toolbar, choose **Open Program**
* In the file selector dialog that appears, choose the Python script you want to run and click **Open**. The script will load into the main editing area of the **Edit Macro** window.
* Click the **Run macro** button in the toolbar of the **Edit Macro** window to run the macro. An extra **Output** window will appear, and log the output of the script as it runs, including any errors.

## Important: Set GLYPHNAMES\_JSON\_FILEPATH at the top of the script
Apart from **add_anchors.py**, all of the supplied script relies on the presence of the **glyphnames.json** metadata file that is part of the main SMuFL distribution. [Download the metadata zip file](http://www.smufl.org/download/), and unzip it to a known location.

In the **Edit Macro** window in FontLab Studio, find the line that reads:

```
GLYPHNAMES_JSON_FILEPATH = ''
```

and between the two single quote marks, write the *fully qualified* path to the location of the **glyphnames.json** file, e.g. on OS X:

```
GLYPHNAMES_JSON_FILEPATH = '/Users/daniel/Desktop/glyphnames.json'
```

If you do not fill in this section correctly, you will see an error message to this effect in the **Output** window.

## Summary of available scripts

### create_glyph_ranges.py
Creates empty glyphs in a font project, and annotates them with the appropriate glyph name in the Note field of each glyph.

This script is useful to set up a new SMuFL-compliant font. Decide which ranges of characters you want to include in your font by referring to the [SMuFL specification](http://www.smufl.org/browse), and uncomment those lines at the top of the script before running it.

### annotate_glyphs_with_smufl_names.py
Annotates glyphs with code points matching those defined in the SMuFL specification with the appropriate glyph name in the Note field of each glyph.

If you already have a SMuFL-compliant font and wish to export the JSON metadata, run this script first to ensure that all of the glyphs in the font have the correct canonical name. The script that exports the font metadata will use the string stored in each glyph's Note field as the primary key for each glyph's metadata in the **glyphsWithAnchors** and **glyphBBoxes** structures.

### generate_font_metadata.py
Exports a JSON file containing the **fontName**, **fontVersion**, **engravingDefaults**, **glyphBBoxes**, **glyphsWithAnchors**, and **optionalGlyphs** metadata.

Before running this script, you should check the values in the `font_metadata` block near the top of the script to ensure the values for the **engravingDefaults** structure are as desired for your specific font. (The default values are taken from those used for Bravura.)

You should also run the **annotate_glyphs_with_smufl_names.py** script if you have not already done so.

You do not need to take any specific action to ensure that the glyph bounding boxes are exported correctly: these can be determined automatically.

However, you should manually add the appropriate anchors to individual glyphs, as described in the **Notes for implementers** section of the SMuFL specification. Refer to **Anchors layer** in **Chapter 6: The Glyph Window** in the FontLab Studio 5 documentation for detailed instructions.

You should also use **Add Note...** (found in the contextual menu for each glyph) to add a note to each glyph in the optional range (U+F400–U+FFFF) containing the glyph name. The **optionalGlyphs** structure is only populated with glyphs that have names specified in their notes.

### make_text_font.py
From a given font intended for use in scoring applications, creates a font intended for use in text-based applications.

It does this by saving a copy of the open font file, adjusting the various names (to add **Text** to the end), then makes adjustments to the font metrics, glyph scaling, and glyph registration as required to handle the differences in guidelines between fonts intended for scoring and text-based applications.

The script also creates ligatures for ranges of characters that are intended to be combined with the control characters in the **Combining staff positions** range, and will create a suitable **liga** OpenType feature table (or append entries to the existing one, if present).

### add_anchors.py
Adds the recommended anchor points for things like glyph cut-outs, stem attachment points for noteheads, optical centers for dynamics, and so on to your font, using the values from the Bravura metadata file, to save the labour of manually adding and correctly naming the anchor points to each glyph individually. After running the script, you will need to manually adjust and check the position of every anchor point, as the position of each anchor point is simply set using its value from the Bravura metadata file.

This script relies on the Note field for each glyph being set to the appropriate SMuFL glyph name to identify the destination glyphs. As such, you should run the **annotate_glyphs_with_smufl_names.py** script if you have not already done so.

Finally, before running this script, ensure you have the **bravura_metadata.json** file in an accessible location. Then, in the **Edit Macro** window in FontLab Studio, find the line that reads:

```
BRAVURA_METADATA_JSON_FILEPATH = ''
```

and edit this to the fully qualified path to the location of the metadata file.

### pua_to_unicode_musical_symbols.py
Copies glyphs with duplicates in the 'Miscellaneous Symbols' or 'Musical Symbols' Unicode ranges to their appropriate alternate code points as components.

Components in existing glyphs will be decomposed before the duplicate glyphs are generated.

## Other FontLab scripts
Knut Nergaard ([@knutnergaard](https://github.com/knutnergaard)) has made a number of scripts for FontLab Studio 5 available at his [FontLab-Scripts](https://github.com/knutnergaard/FontLab-Scripts/tree/main/SMuFL) repository, and he welcomes [donations](https://github.com/knutnergaard/FontLab-Scripts) if you find them useful.