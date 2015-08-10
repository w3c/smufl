### ligatures

The "ligatures" structure contains a list of ligatures defined in the
font. Applications that cannot access advanced font features like
OpenType ligatures can instead determine the presence of a ligature that
joins together a number of recommended glyphs, and its code point, using
this data.

Below is an excerpt from a dummy font metadata file for Bravura, with a
section of the "ligatures" structure filled in:

```
{
  ...
  "ligatures": {
    "accidentalDoubleFlatParens": {
      "codepoint": "U+F530",
      "componentGlyphs": [
        "accidentalParensLeft",
        "accidentalDoubleFlat",
        "accidentalParensRight"
      ]
    },
    ...
  }
...
}
```

The structure uses the name of the ligature as its key, and the values
include its code point, and its component glyphs. The component glyphs
should be listed in an array called "componentGlyphs", in the same order
as they are listed in e.g. the liga OpenType table.
