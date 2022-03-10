### glyphsWithAnchors

The "glyphsWithAnchors" structure contains a structure for each glyph
for which metadata is supplied, with the canonical glyph name as the
key. Each glyph may define any of the following key/value pairs:

| *Key name* | *Description*
| ---------- | --------------------------
| "splitStemUpSE" | The exact position at which the bottom right-hand (south-east) corner of an angled upward-pointing stem connecting the right-hand side of a notehead to a vertical stem to its left should start, relative to the glyph origin, expressed as Cartesian coordinates in staff spaces.
| "splitStemUpSW" | The exact position at which the bottom left-hand (south-west) corner of an angled upward-pointing stem connecting the left-hand side of a notehead to a vertical stem to its right should start, relative to the glyph origin, expressed as Cartesian coordinates in staff spaces.
| "splitStemDownNE" | The exact position at which the top right-hand (north-east) corner of an angled downward-pointing stem connecting the right-hand side of a notehead to a vertical stem to its left should start, relative to the glyph origin, expressed as Cartesian coordinates in staff spaces.
| "splitStemDownNW" | The exact position at which the top left-hand (north-west) corner of an angled downward-pointing stem connecting the left-hand side of a notehead to a vertical stem to its right should start, relative to the glyph origin, expressed as Cartesian coordinates in staff spaces.
| "stemUpSE" | The exact position at which the bottom right-hand (south-east) corner of an upward-pointing stem rectangle should start, relative to the glyph origin, expressed as Cartesian coordinates in staff spaces.
| "stemDownNW" | The exact position at which the top left-hand (north-west) corner of a downward-pointing stem rectangle should start, relative to the glyph origin, expressed as Cartesian coordinates in staff spaces.
| "stemUpNW" | The amount by which an up-stem should be lengthened from its nominal unmodified length in order to ensure a good connection with a flag, in spaces.[^11]
| "stemDownSW" | The amount by which a down-stem should be lengthened from its nominal unmodified length in order to ensure a good connection with a flag, in spaces.
| "nominalWidth" | The width in staff spaces of a given glyph that should be used for e.g. positioning leger lines correctly.[^12]
| "numeralTop" | The position in staff spaces that should be used to position numerals relative to clefs with ligated numbers where those numbers hang from the bottom of the clef, corresponding horizontally to the center of the numeral’s bounding box.
| "numeralBottom" | The position in staff spaces that should be used to position numerals relative to clefs with ligatured numbers where those numbers sit on the baseline or at the north-east corner of the G clef, corresponding horizontally to the center of the numeral’s bounding box.
| "cutOutNE" | The Cartesian coordinates in staff spaces of the bottom left corner of a nominal rectangle that intersects the top right corner of the glyph’s bounding box. This rectangle, together with those in the other four corners of the glyph’s bounding box, can be cut out to produce a more detailed bounding box (of abutting rectangles), useful for kerning or interlocking symbols such as accidentals.
| "cutOutSE" | The Cartesian coordinates in staff spaces of the top left corner of a nominal rectangle that intersects the bottom right corner of the glyph’s bounding box.
| "cutOutSW" | The Cartesian coordinates in staff spaces of the top right corner of a nominal rectangle that intersects the bottom left corner of the glyph’s bounding box.
| "cutOutNW" | The Cartesian coordinates in staff spaces of the bottom right corner of a nominal rectangle that intersects the top left corner of the glyph’s bounding box.
| "graceNoteSlashSW" | The Cartesian coordinates in staff spaces of the position at which the glyph graceNoteSlashStemUp should be positioned relative to the stem-up flag of an unbeamed grace note; alternatively, the bottom left corner of a diagonal line drawn instead of using the above glyph.
| "graceNoteSlashNE" | The Cartesian coordinates in staff spaces of the top right corner of a diagonal line drawn instead of using the glyph graceNoteSlashStemUp for a stem-up flag of an unbeamed grace note.
| "graceNoteSlashNW" | The Cartesian coordinates in staff spaces of the position at which the glyph graceNoteSlashStemDown should be positioned relative to the stem-down flag of an unbeamed grace note; alternatively, the top left corner of a diagonal line drawn instead of using the above glyph.
| "graceNoteSlashSE" | The Cartesian coordinates in staff spaces of the bottom right corner of a diagonal line drawn instead of using the glyph graceNoteSlashStemDown for a stem-down flag of an unbeamed grace note.
| "repeatOffset" | The Cartesian coordinates in staff spaces of the horizontal position at which a glyph repeats, i.e. the position at which the same glyph or another of the same group should be positioned to ensure correct tessellation. This is used for e.g. multi-segment lines and the component glyphs that make up trills and mordents.
| "noteheadOrigin" | The Cartesian coordinates in staff spaces of the left-hand edge of a notehead with a non-zero left-hand side bearing (e.g. a double whole, or breve, notehead with two vertical lines at each side), to assist in the correct horizontal alignment of these noteheads with other noteheads with zero-width left-side bearings.
| "opticalCenter" | The Cartesian coordinates in staff spaces of the optical center of the glyph, to assist in the correct horizontal alignment of the glyph relative to a notehead or stem. Currently recommended for use with glyphs in the **Dynamics** range.

Below is an excerpt of a dummy font metadata file for the Bravura font,
with some of the "glyphsWithAnchors" structure filled in:

```
{
  ...
  "glyphsWithAnchors": {
    "noteheadBlack": {
      "stemDownNW": [
        0.0,
        -0.184
      ],
      "stemUpSE": [
        1.328,
        0.184
      ]
    },
    ...
  },
  ...
}
```

[^11]: It is typical for noteheads and flags to be drawn using font glyphs, while stems themselves are drawn using primitive lines or rectangles. Flag glyphs in SMuFL-compliant fonts are registered such that y=0 represents the end of a stem drawn at its normal length, i.e. typically 3.5 staff spaces, so for simple drawing, any flag can be drawn at the same position relative to the stem and give the correct visual stem length. Modern drawing APIs typically provide sub-pixel RGB anti-aliasing for font glyphs, but may only provide grayscale anti-aliasing for primitive shapes. If the stem is drawn at its normal length with a flag glyph continuing beyond the end of the stem, there may be a poor visual appearance resulting from the primitive stem using standard anti-aliasing and the flag glyph using sub-pixel anti-aliasing. Therefore, it is recommended to extend the stem by the additional height of the flag such that the primitive stem stops at the end (or just short of the end) of the flag. Because the amount by which the stem should be extended is highly dependent on the design of the flag in a particular font, this value should be specified for each flag glyph in the metadata JSON file.

[^12]: Certain fonts, for example those that mimic music calligraphy, may include glyphs that are asymmetric by design, and where a simple calculation of the glyph’s bounding box will not provide the correct result for registering that glyph with other primitives. For example, a whole rest may be slightly oblique if mimicking a chisel nib pen, and for precise registration it may be necessary to specify its width independent of the glyph’s actual bounding box.
