Metrics and glyph registration for text-based applications
----------------------------------------------------------

The following guidelines are provided for fonts intended for use in
text-based applications, such as word processors, desktop publishers and
other text editors.

Upper case letters in a text font do not typically occupy the whole
height of the em square: instead, they typically occupy around 75–80% of
the height of the em square, with the key metrics for ascender and caps
height both falling within this range. In order for the line spacing of
a font containing music characters to be equivalent to that of a text
font, its key metrics must match, i.e. the ascender, caps height and
descender must be very similar. Glyphs with unusually large ascenders
and descenders (such as notes of short duration with multiple flags)
should not be scaled individually in order to fit within the ascender
height, as they will not then fit with the other glyphs at the same
point size; however, the behavior of glyphs that extend beyond the
font’s ascender and descender metrics is highly variable between
different applications.

Leading on from the premise that a SMuFL-compliant font for text-based
applications should use metrics compatible with regular text fonts,
specific guidelines are as follows:

-   Dividing 80% of the height of the em in four provides an analogue
    for a five-line staff. If a font uses 1000 upm (design units per
    em), as is conventional for a PostScript font, the height of a
    five-line staff is 800 design units, or 0.8 em; therefore, one staff
    space height is 200 design units, or 0.2 em. If a font uses
    2048 upm, as is conventional for a TrueType font, the height of a
    five-line staff is 1640 design units, and one staff space is 410
    design units.

-   The origin (bottom left corner of the em square, i.e. x = 0 and y =
    0 in font design space) therefore represents the middle of the
    bottom staff line of a nominal five-line staff, and y = 0.8 em
    represents the middle of the top staff line of that same
    five-line staff.

-   Unless otherwise stated, all glyphs should be drawn at a scale
    consistent with the key measurement that one staff space = 0.2 em.

-   Unless otherwise stated, all glyphs shall be horizontally registered
    so that their leftmost point coincides with x = 0.

-   Unless otherwise stated, all glyphs shall have zero-width side
    bearings, i.e. no blank space to the left or right of the glyph.

-   Staff line and leger line glyphs should have an advance width of
    zero, so that other glyphs can be drawn on top of them easily.

-   Time signature digits should also have an advance width of zero, so
    that they can be positioned above each other (using the
    **timeSigCombNumerator** and **timeSigCombDenominator** ligatures).

-   Clefs should be positioned such that they are aligned with the
    five-line staff glyphs (e.g. staff5lines) at their most usual staff
    position: G clefs (in the class clefsG) should be positioned such
    that the bottom loop is aligned with the bottom staff line (0.2 em
    higher than the position in a SMuFL-compliant font for a scoring
    application); F clefs (in the class clefsF) should be positioned
    such that the second-highest staff line passes between the two dots
    (0.6 em higher than in a font for a scoring application); and C
    clefs (in the class clefsC) should be positioned such that the
    middle staff line passes through the middle of the clef (0.4 em
    higher than in a font for a scoring application).[^14]

-   Glyphs that can appear at different staff positions, e.g. noteheads,
    notes, accidentals, etc. (in class combiningStaffPositions), should
    be positioned such that they are centered around the middle staff
    line of the five-line staff glyphs (i.e. centered vertically around
    y = 0.4 em).

-   To enable the positioning of glyphs at different staff positions,
    fonts should support the combination of combining staff position
    control characters and glyphs in the class combiningStaffPositions
    using a glyph substitution feature such as OpenType ligatures. This
    allows the end user to position e.g. a black notehead on the
    second-highest staff line by using a ligature of **staffPosRaise2**
    and **noteheadBlack**.

-   Letters for dynamics and numbers for octave lines should be scaled
    such that the x-height is around 0.5 em, consistent with other
    typical text fonts.

-   Ornaments symbols should be scaled such that e.g. the <span class="bravura">&#xe566;</span> symbol is
    around 0.5 em in height (e.g. a scale factor of 150% compared to
    fonts intended for use in scoring applications).

-   Keyboard pedal marks should be scaled such that e.g. the <span class="bravura">&#xE650;</span> symbol is
    around 0.75 em in height (e.g. a scale factor of 130% compared to
    fonts intended for use in scoring applications).

-   Percussion pictograms should be scaled such that they are around
    0.75 em in height.

-   Figured bass digits should be scaled such that e.g. <span class="bravura">&#xEA58;</span> is around 0.5
    em in height (e.g. a scale factor of 185% compared to fonts intended
    for use in scoring applications).

-   Composite note glyphs for setting in-line with characters from other
    text fonts (e.g. those in the **Metronome marks** range) should be
    positioned such that they sit on the font baseline (in contrast to
    notes intended for drawing on a staff, e.g. those in the
    **Individual notes** range).

[^14]: The recommended default placement for C clefs is on the middle staff line, i.e. as an alto clef. Positioning the C clef such that it is centered around the second-highest staff line, i.e. as a tenor clef, can be achieved using the combining staff position control characters, if the font implements ligatures or other glyph substitution features.
