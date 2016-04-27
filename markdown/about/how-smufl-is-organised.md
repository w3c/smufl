How SMuFL is organized
----------------------

The aim of the Standard Music Font Layout (SMuFL) is to provide the
basis for music font mapping for the age of Unicode and OpenType fonts.

SMuFL uses the standard Private Use Area in the Basic Multilingual Plane
(starting at code point U+E000), and currently includes just over 2440
recommended characters, plus several hundred further optional but
recommended glyphs, primarily ligatures (i.e. two or more symbols drawn
as a single glyph) and stylistic alternates (i.e. a different appearance
for the same character with equivalent meaning). SMuFL is a superset of
the Unicode Musical Symbols range, and it is recommended that common
characters are included both at code points in SMuFL and in the Unicode
Musical Symbols range. In the tables of glyphs in this document, where
glyphs are shared between SMuFL and the Unicode Musical Symbols range,
the Unicode Musical Symbols code point is shown following the SMuFL code
point.

The groupings of characters within SMuFL are based on the groupings
defined by Perry Roland in the Unicode Musical Symbols range, but with
finer granularity. There are currently 118 groups of characters,
proceeding roughly in order from least to most idiomatic, i.e. specific
to particular instruments, types of music, or historical periods. The
grouping has no significance other than acting as an attempt to provide
an overview of the included characters.

Room for future expansion has generally been left in each group, so code
points are not contiguous. The code point of each character in SMuFL 1.0
is intended to be immutable, and likewise every character has a
canonical name, also intended to be immutable.
