### glyphsWithAlternates

The "glyphsWithAlternates" structure contains a list of the glyphs in
the font for which stylistic alternates are provided, together with
their name and code point. Applications that cannot access advanced font
features like OpenType stylistic alternates can instead determine the
presence of an alternate for a given glyph, and its code point, using
this data.

Below is an excerpt from a dummy font metadata file for Bravura, with a
section of the "glyphsWithAlternates" structure filled in:

```
{
  ...
  "glyphsWithAlternates": {
    "flag8thUp": {
      "alternates": [
        {
          "codepoint": "U+F410",
          "name": "flag8thUpStraight",
        },
        {
          "codepoint": "U+F411",
          "name": "flag8thUpShort"
        }
      ]
    },
    "gClef": {
      "alternates": [
        {
          "codepoint": "U+F470",
          "name": "gClefSmall"
        }
      ]
    },
  ...
}
```

For each recommended glyph for which one or more alternates is provided,
the "alternates" structure provides an array containing the name and
code point of each alternate. Font designers are encouraged to use a
consistent naming scheme for alternates.
