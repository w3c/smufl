## glyphnames.json

glyphnames.json maps code points to canonical glyph names, which by
convention use lower camel case, a convenient format for most
programming languages. Here is an excerpt of this file:

```
{
...
  "barlineDashed": {
    "alternateCodepoint": "U+1D104",
    "codepoint": "U+E036",
    "description": "Dashed barline"
  },
  "barlineDotted": {
    "codepoint": "U+E037"
    "description": "Dotted barline"
  },
  "barlineDouble": {
    "alternateCodepoint": "U+1D101",
    "codepoint": "U+E031"
    "description": "Double barline"
  },
  "barlineFinal": {
    "alternateCodepoint": "U+1D102",
    "codepoint": "U+E032"
    "description": "Final barline"
  },
    "barlineHeavy": {
    "codepoint": "U+E034"
    "description": "Heavy barline"
  },
...
}
```

The file is keyed using the glyph names, with the SMuFL code point
provided as the value for the "codepoint" key, and the Unicode Musical
Symbols range code point (if applicable) provided as the value for the
"alternateCodepoint" key. The "description" key contains the glyph’s
description, as it appears in this specification.
