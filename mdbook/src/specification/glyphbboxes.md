### glyphBBoxes

The optional "glyphBBoxes" structure contains information about the
actual bounding box for each glyph.[^13] The glyph bounding box is
defined as the smallest rectangle that encloses every part of the
glyph’s path, and is described as a pair of coordinates for the
bottom-left (or southwest) and top-right (or northeast) corners of the
rectangle, expressed staff spaces to any required degree of precision,
relative to the glyph origin.

Below is an excerpt from a dummy font metadata file for Bravura, with a
section of the "glyphBBoxes" structure filled in:

```
{
...
  "glyphBBoxes":
  {
    "brace": {
      "bBoxNE": [
        0.328,
        3.988
      ],
      "bBoxSW": [
        0.008,
        0.0
      ]
    },
    "braceFlat": {
      "bBoxNE": [
        0.36,
        4.084
      ],
      "bBoxSW": [
        0.0,
        0.004
      ]
    },
  ...
  }
}
```

For each glyph, the "glyphBBoxes" structure provides the glyph’s name
and the coordinates of the opposite corners of the bounding rectangle
(keys bBoxSW and bBoxNE).

[^13]: This data is provided primarily for MakeMusic Finale, which requires bounding box data for certain graphical and spacing calculations performed by the software. This information is stored in a per-font data file called a Font Annotation (FAN) file, and can be edited directly within Finale in the Font Annotation dialog. Font designers who choose to provide this information for SMuFL-compliant fonts can save end users the steps of creating Font Annotation files in Finale, as future versions of Finale may be able to consume this metadata directly and automatically produce the required Font Annotation file.
