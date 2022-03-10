## ranges.json

ranges.json provides information about the way glyphs are presented in
discrete ranges in this specification. Here is an excerpt of this file:

```
{
  ...
  "analytics": {
    "description": "Analytics",
    "glyphs": [
      "analyticsHauptstimme",
      "analyticsNebenstimme",
      "analyticsStartStimme",
      "analyticsEndStimme",
      "analyticsTheme",
      "analyticsThemeRetrograde",
      "analyticsThemeRetrogradeInversion",
      "analyticsThemeInversion",
      "analyticsTheme1",
      "analyticsInversion1"
    ],
    "range_end": "U+E86F",
    "range_start": "U+E860"
  }
  ...
}
```

This file uses a unique identifier for each range as the primary key,
and within each structure the “description” specifies the human-readable
range name (as it appears in this specification), “glyphs” is an array
listing the canonical names of the glyphs contained within the range,
and the “range\_start” and “range\_end” key/value pairs specify the
first and last code point allocated to this range respectively.

The current versions of glyphnames.json, classes.json and ranges.json
are available for download at
[GitHub](https://github.com/w3c/smufl/tree/gh-pages/metadata).

It is further recommended that SMuFL-compliant fonts also contain
font-specific metadata JSON files, which are described below.
