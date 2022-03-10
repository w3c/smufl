Metrics and glyph registration for scoring applications
-------------------------------------------------------

The following guidelines are provided for fonts intended for use in scoring
applications:

-   Dividing the em in four provides an analogue for a five-line staff:
    if a font uses 1000 upm (design units per em), as is conventional
    for a PostScript font, one staff space is equal to 250 design units;
    if a font uses 2048 upm, as is conventional for a TrueType font, one
    staff space is equal to 512 design units.

-   The origin (bottom left corner of the em square, i.e. x = 0 and y =
    0 in font design space) therefore represents the middle of the
    bottom staff line of a nominal five-line staff, and y = 1 em
    represents the middle of the top staff line of that same
    five-line staff.

-   All glyphs should be drawn at a scale consistent with the key
    measurement that one staff space = 0.25 em.

-   Unless otherwise stated, all glyphs shall be horizontally registered
    so that their leftmost point coincides with x = 0.

-   Unless otherwise stated, all glyphs shall have zero-width side
    bearings, i.e. no blank space to the left or right of the glyph.

-   Glyphs that apply to a staff as a whole (e.g. barlines) shall be
    registered such that the font baseline lies at the nominal vertical
    position of the bottom line of a five-line staff. If the glyph is
    specific to a staff other than a regular five-line staff, then for
    registration purposes that staff’s vertical center shall be exactly
    aligned with the vertical center of a five-line staff.

-   Glyphs for movable notations that apply to some vertical staff
    position (e.g. noteheads, accidentals) shall be registered such that
    the font baseline lies exactly at that position. For example, a
    typical notehead or accidental glyph is registered such that it is
    vertically centered on the baseline.

-   Clefs should be positioned such that the pitch the clef refers to
    is on the baseline (e.g. the F clef is placed such that the upper
    dot is above and the lower dot below the baseline). If a clef does
    not refer specifically to a pitch, its y=0 should coincide with the
    center staff line on a five-line staff, or the visual center for
    staves with more or fewer than five lines (e.g. tablature staves).

-   Noteheads should be positioned as if on the bottom line of the staff
    (except for complete clusters representing intervals of a second or
    third, which should be positioned as if in the bottom space of
    the staff).

-   Pre-composed stems should be positioned as if they are pointing
    upwards and attached to a notehead on the bottom line of the staff.
    The center of the stem should be at x=0.

-   Combining glyphs that are designed to be superimposed on stems
    (stem decorations) should be registered such that the point that
    should sit in the center of the stem (i.e. typically the visual
    center of the symbol) should be at x=0 and y=0.

-   Accidentals should be positioned as if they apply to a notehead on
    the bottom line of the staff.

-   Articulations to be positioned above a note or chord should be
    positioned such that they sit on the baseline (y=0), while
    articulations to be positioned below a note or chord should be
    positioned such that they hang from the baseline.

-   Pre-composed notes should be positioned as if on the bottom line of
    the staff.

-   Flags are positioned such that y=0 corresponds to the end of a stem
    of normal length, and such that x=0 corresponds to the left-hand
    side of the stem.

-   Rests are relative to an imaginary staff position, typographically
    speaking (usually the center line of a five-line staff in which the
    rest assumes its default position). The font baseline should
    represent this staff position, with the exception of the whole
    note (semibreve) rest, which should hang from the font baseline.

-   Bracket ends are positioned such that the point at which they
    connect to the top or bottom of a vertical bracket is at y=0.

-   Letters for dynamics (and for D.C./D.S. in the repeats range) should
    be scaled such that the caps height is around 0.5 em, and the
    x-height is around 0.25 em. Letters for dynamics should also have
    non-zero side bearings to achieve good default spacing when set in a
    single run.

-   Digits for time signatures should be scaled such that each digit is
    two staff spaces tall, i.e. 0.5 em, and vertically centered on
    the baseline. Although some glyphs in the time signatures range
    (such as the large + sign, common and cut time glyphs, etc.) apply
    to the whole staff, these should likewise be vertically centered on
    the baseline. Time signature digits should also have non-zero side
    bearings to achieve good default spacing when set in a single run.

-   Parentheses (for accidentals, time signatures, figured bass, etc.)
    may have non-zero side bearings, in order to achieve good default
    spacing when set in a single run with the glyphs they are intended
    to bracket.

-   Figured bass digits and function theory symbols should have non-zero
    side bearings to achieve good default spacing when set in a
    single run.

-   Tessellating glyphs (such as wavy lines, or the component parts of
    complex trills and mordents) should have negative side bearings, in
    order to achieve correct tessellation when set in a single run.

Many of these guidelines are based on the conventions established by
Adobe’s Sonata font and carried through by most other fonts designed for
use in scoring applications, for the sake of making it as easy as
possible for font and application developers to transition their
existing fonts and software to supporting SMuFL-compliant fonts.
