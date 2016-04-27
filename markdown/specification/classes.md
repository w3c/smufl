## classes.json

classes.json groups glyphs together into classes, so that software
developers can handle similar glyphs (e.g. noteheads, clefs, flags,
etc.) in a similar fashion. Here is an excerpt of this file:

```
{
...
  "clefs": [
    "gClef",
    "gClef15mb",
    "gClef8vb",
    "gClef8va",
    "gClef15ma",
    "gClef8vbOld",
    "gClef8vbCclef",
    ...
  ],
  "noteheads": [
    "noteheadDoubleWhole",
    "noteheadWhole",
    "noteheadHalf",
    "noteheadBlack",
    "noteheadNull",
    ...
  ],
  "flags": [
    "flag8thUp",
    "flag8thDown",
    "flag16thUp",
    "flag16thDown",
    "flag32ndUp",
    "flag32ndDown",
    ...
  ],
...
}
```

Glyphs are listed within their classes using the names specified in
glyphnames.json. Not all glyphs are contained within classes, and the
same glyph can appear in multiple classes.

The classes defined at present are as follows:

| *Class name*                      | *Description*
| --------------------------------- | -------------------------
| accidentals                       | Contains all glyphs in all accidentals ranges.
| accidentals24EDOArrows, accidentals53EDOTurkish, accidentals72EDOWyschnegradsky, accidentalsAEU, accidentalsArabic, accidentalsHelmholtzEllis, accidentalsJohnston, accidentalsPersian,  accidentalsSagittalAthenian, accidentalsSagittalDiacritics, accidentalsSagittalMixed, accidentalsSagittalPromethean, accidentalsSagittalPure, accidentalsSagittalTrojan, accidentalsSims, accidentalsStandard, accidentalsSteinZimmermann, accidentalsStockhausen | These classes contain useful subsets of accidentals, each class essentially providing all of the accidentals glyphs required for a given convention or system.
| articulations                     | Contains all articulations, regardless of whether they are intended to be positioned above or below the note/staff.
| articulationsAbove, articulationsBelow | Contains only those articulations that are positioned either above or below the note/staff, as appropriate.
| combiningStaffPositions           | Contains glyphs that are available in ligatures with the Combining staff position glyphs, in fonts intended for use in text-based applications. (N.B. not implemented in the current Bravura font, which is intended for scoring applications.)
| clefs                             | Contains all clefs, regardless of the position on the staff at which they are typically positioned.
| clefsC                            | Contains all C clefs.
| clefsF                            | Contains all F clefs.
| clefsG                            | Contains all G clefs.
| dynamics                          | Contains the glyphs in the **Dynamics** range, which should be scaled differently to other glyphs in fonts designed for use in text-based applications.
| forTextBasedApplications          | Contains glyphs that scoring applications can generally ignore, i.e. these are useful for text-based applications (or for runs of normal text in scoring applications). This contains glyphs like the **Beamed groups of notes** range, pre-composed stems, pre-composed staff lines, etc.
| multiGlyphForms                   | Contains all glyphs that are designed to be used in combination to produce larger forms, e.g. ornaments, wiggly lines, etc.
| noteheads                         | Contains all glyphs in all noteheads ranges.
| noteheadSetCircled, noteheadSetCircleX, noteheadSetDefault, noteheadSetDiamond, noteheadSetDiamondOld, noteheadSetHeavyX, noteheadSetLargeArrowDown, noteheadSetLargeArrowUp, noteheadSetNamesPitch, noteheadSetNamesSolfege, noteheadSetPlus, noteheadSetRoundLarge, noteheadSetRoundSmall, noteheadSetSacredHarp, noteheadSetSlashed1, noteheadSetSlashed2, noteheadSetSlashHorizontalEnds, noteheadSetSlashVerticalEnds, noteheadSetSquare, noteheadSetTriangleDown, noteheadSetTriangleLeft, noteheadSetTriangleRight, noteheadSetTriangleUp, noteheadSetWithX, noteheadSetX, parenthesesNotehead | These classes contain useful subsets of noteheads, each class providing a set of noteheads, e.g. the notehead to be used for quarter notes and shorter, for half notes, for whole notes, etc., for different conventions.
| octaves                           | Contains all glyphs relating to octave lines.
| ornaments                         | Contains all pre-composed ornament glyphs, excluding the component parts in the Combining strokes for trills and mordents range.
| pauses                            | Contains all fermatas/caesuras, regardless of whether they are intended to be positioned above or below the note/staff.
| pausesAbove, pausesBelow          | Contains only those fermatas that are positioned either above or below the note/staff, as appropriate.
| rests                             | Contains all rests glyphs.
| stemDecorations                   | Contains glyphs that are designed to be positioned on stems. This is a useful class, because the individual glyphs that are intended to be drawn on stems are dotted around various ranges.
| wigglesArpeggiato, wigglesArpeggiatoDown, wigglesArpeggiatoUp, wigglesCircularMotion, wigglesQuasiRandom, wigglesTrill, wigglesVibrato, wigglesVibratoVariable | These classes contain useful subsets of the Multi-segment lines range.
