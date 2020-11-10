### engravingDefaults

The "engravingDefaults" structure contains key/value pairs defining
recommended defaults for line widths etc., as follows, with all
measurements expressed in staff spaces:

| *Key name*                     | *Description*
| ------------------------------ | --------------------------------------------
| "textFontFamily"               | An array containing the text font family (or families, in descending order of preference) that are ideally paired with this music font; this list may also use the generic font family values defined in [CSS](https://www.w3.org/TR/CSS2/fonts.html#generic-font-families), i.e. **serif**, **sans-serif**, **cursive**, **fantasy**, and **monospace**. Generic font family names should be listed after specific font families.
| "staffLineThickness"           | The thickness of each staff line
| "stemThickness"                | The thickness of a stem
| "beamThickness"                | The thickness of a beam
| "beamSpacing"                  | The distance between the inner edge of the primary and outer edge of subsequent secondary beams
| "legerLineThickness"           | The thickness of a leger line (normally somewhat thicker than a staff line)
| "legerLineExtension"           | The amount by which a leger line should extend either side of a notehead, scaled proportionally with the notehead's size, e.g. when scaled down as a grace note
| "slurEndpointThickness"        | The thickness of the end of a slur
| "slurMidpointThickness"        | The thickness of the mid-point of a slur (i.e. its thickest point)
| "tieEndpointThickness"         | The thickness of the end of a tie
| "tieMidpointThickness"         | The thickness of the mid-point of a tie
| "thinBarlineThickness"         | The thickness of a thin barline, e.g. a normal barline, or each of the lines of a double barline
| "thickBarlineThickness"        | The thickness of a thick barline, e.g. in a final barline or a repeat barline
| "dashedBarlineThickness"       | The thickness of a dashed barline
| "dashedBarlineDashLength"      | The length of the dashes to be used in a dashed barline
| "dashedBarlineGapLength"       | The length of the gap between dashes in a dashed barline
| "barlineSeparation"            | The default distance between multiple thin barlines when locked together, e.g. between two thin barlines making a double barline, measured from the right-hand edge of the left barline to the left-hand edge of the right barline.
| "thinThickBarlineSeparation"   | The default distance between a pair of thin and thick barlines when locked together, e.g. between the thin and thick barlines making a final barline, or between the thick and thin barlines making a start repeat barline. 
| "repeatBarlineDotSeparation"   | The default horizontal distance between the dots and the inner barline of a repeat barline, measured from the edge of the dots to the edge of the barline.
| "bracketThickness"             | The thickness of the vertical line of a bracket grouping staves together
| "subBracketThickness"          | The thickness of the vertical line of a sub-bracket grouping staves belonging to the same instrument together
| "hairpinThickness"             | The thickness of a *crescendo*/*diminuendo* hairpin
| "octaveLineThickness"          | The thickness of the dashed line used for an octave line
| "pedalLineThickness"           | The thickness of the line used for piano pedaling
| "repeatEndingLineThickness"    | The thickness of the brackets drawn to indicate repeat endings
| "arrowShaftThickness"          | The thickness of the line used for the shaft of an arrow
| "lyricLineThickness"           | The thickness of the lyric extension line to indicate a melisma in vocal music
| "textEnclosureThickness"       | The thickness of a box drawn around text instructions (e.g. rehearsal marks)
| "tupletBracketThickness"       | The thickness of the brackets drawn either side of tuplet numbers
| "hBarThickness"                | The thickness of the horizontal line drawn between two vertical lines, known as the H-bar, in a multi-bar rest

Below is a dummy "engravingDefaults" structure, with some of the values
filled in:

```
{
  ...
  "engravingDefaults": {
    "textFontFamily" : [ "Academico", "Century Schoolbook", "serif" ],
    "staffLineThickness": 0.1,
    "stemThickness": 0.1,
    "beamThickness": 0.5,
    "beamSpacing": 0.25,
    "legerLineThickness": 0.2,
    "legerLineExtension": 0.2,
    ...
  },
  ...
}
```
