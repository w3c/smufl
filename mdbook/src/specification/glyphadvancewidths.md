### glyphAdvanceWidths

The optional "glyphAdvanceWidths" structure describes the advance width of each glyph. The advance width is defined as the width of a glyph as measured from its origin to the origin of the next glyph on the line. In text fonts for many languages, glyphs normally have positive left and right side-bearings, i.e. space to either side of the glyph, so that a string of glyphs will show the expected letter spacing. The advance width includes these side-bearing values. If a glyph's path protrudes _beyond_ the width defined for the glyph in the font, however, these protrusions to the left or the right – which can be termed negative side-bearings – are not included in the advance width.

In SMuFL fonts, glyphs typically have zero left and right side-bearings, and some glyphs may have negative side-bearings. For example, **stemSulPonticello** has a very narrow width, and large negative side-bearings to accommodate the _sul ponticello_ sign that is centered on the stem.

Values in the "glyphAdvanceWidths" structure are expressed as a single value in staff spaces, to any required degree of precision.

Below is an excerpt from a dummy font metadata file for Bravura, with a section of the "glyphAdvanceWidths" structure filled in:

```
{
...
  "glyphAdvanceWidths":
  {
    "analyticsNebenstimme": 2.836,
    "figbass9": 0.944,
    "pictBeaterSoftBassDrumDown": 1.28,
    "wiggleCircularEnd": 0.648,
  ...
  }
}
```

For each glyph, the "glyphAdvanceWidths" structure provides the glyph’s name and its advance width.