This range is intended for mixing music symbols with text. Its metrics
and glyph registrations should follow the guidelines for fonts intended
for text-based applications, even in fonts that are themselves primarily
intended for use in scoring applications.

These glyphs may be used for displaying complex metric modulations and
*l’istesso tempo* directions in conjunction with the precomposed note
glyphs in the **Individual notes** range.

Kerning pairs for every combination of these glyphs should be included
such that the fractional beams overlap slightly with the stems of notes
and other beams; this helps provide a consistent appearance in a variety
of rendering contexts and at different zoom levels. Special attention
should be given to the kerning pairs including **textAugmentationDot**,
which should be kerned rightwards away from notes and leftwards so that
it lies underneath glyphs showing the middle of beams (e.g.
**textCont8thBeamShortStem**); and to the pairs involving the tuplet
brackets (e.g. **textTupletBracketStartShortStem**), which should be kerned
leftwards such that they are correctly aligned when entered after a note
character.

By way of example:

| **Example** | **Uses glyphs** |
| ----------- | --------------- |
| ![](../media/beamed-8ths-16ths.png) | textBlackNoteShortStem, textCont8thBeamShortStem, textBlackNoteFrac8thShortStem, textCont16thBeamShortStem, textBlackNoteFrac16thShortStem
| ![](../media/beamed-8ths-equals-triplet.png) | textBlackNoteShortStem, textCont8thBeamShortStem, textBlackNoteFrac8thShortStem, space, =, space, textBlackNoteShortStem, textTupletBracketStartLongStem, textTuplet3LongStem, note8thUp, textTupletBracketEndLongStem
| ![](../media/beamed-dotted-8th-16th.png) | textBlackNoteShortStem, textCont8thBeamShortStem, textAugmentationDot, textCont8thBeamShortStem, textBlackNoteFrac16thShortStem
