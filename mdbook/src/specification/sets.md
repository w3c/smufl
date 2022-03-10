### sets

The "sets" structure contains a list of stylistic sets defined in the
font. Applications that cannot access advanced font features like
OpenType stylistic sets can instead determine the presence of sets in a
font, the purpose of each set, and the name and code point of each glyph
in each set, using this data.

The purpose of each set is specified by the "type" key, which can have
any of the following values:

| *Value*                | *Description*
| ---------------------- | ------------------------------------------------------------
| "opticalVariantsSmall" | Glyphs designed for use on smaller staff sizes.
| "flagsShort"           | Alternate shorter flags for notes with augmentation dots.
| "flagsStraight"        | Alternate flags that are straight rather than curved.
| "timeSigsLarge"        | Alternate time signature digits for use outside the staff.
| "noteheadsLarge"       | Alternate oversized noteheads.

The current list of values for "type" are based on the sets present in
Bravura. If you are a font designer and wish to add other sets to your
own font, please propose a new value and description for the "type" key
to the SMuFL community so that it can be discussed and subsequently
added to the above list in a future revision.

Below is an excerpt from a dummy font metadata file for Bravura, with a
section of the "sets" structure filled in:

```
{
...
  "sets": {
    "ss01": {
      "type": "opticalVariantsSmall",
      "description": "Smaller optical size for small staves",
      "glyphs": [
        {
          "codepoint": "U+F428",
          "name": "accidentalFlatSmall",
          "alternateFor": "accidentalFlat"
        },
        {
          "codepoint": "U+F429",
          "name": "accidentalNaturalSmall",
          "alternateFor": "accidentalNatural"
        },
        {
          "codepoint": "U+F42A",
          "name": "accidentalSharpSmall",
          "alternateFor": "accidentalSharp"
        },
        ...
      ],
    },
    "ss02": {
      "type": "FlagsShort",
      "description": "Short flags (to avoid augmentation dots)",
      "glyphs": [
        {
          "codepoint": "U+F411",
          "name": "flag8thUpShort",
          "alternateFor": "flag8thUp"
        },
        {
          "codepoint": "U+F414",
          "name": "flag16thUpShort",
          "alternateFor": "flag16thUp"
        },
        ...
      ],
    },
  ...
  }
...
}
```

The structure uses the name of the set as its key, and the values include the
code point and name of the alternate glyph, together with the name of the
character for which this is an alternate ("alternateFor").
