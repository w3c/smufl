Designing for scoring applications and text-based applications
--------------------------------------------------------------

In addition to providing a standard approach to how musical symbols
should be assigned to Unicode code points, SMuFL also aims to provide
two sets of guidelines for the metrics and glyph registration,
addressing the two most common use cases for fonts that contain musical
symbols, i.e. use within dedicated scoring applications, and use within
text-based applications (such as a word processors, desktop publishers,
web pages, etc.).

Since it is helpful for scoring applications that all symbols in a font
be scaled relative to each other as if drawn on a staff of a particular
size, and conversely it is helpful for musical symbols to be drawn
in-line with text to be scaled relative to the letterforms with which
the musical symbols are paired, in general a single font cannot address
these two use cases: the required metrics and relative scaling of glyphs
are incompatible[^10].

Therefore, it is recommended that font developers make clear whether a
given font is intended for use by scoring applications or by text-based
applications by appending “Text” to the name of the font intended for
text-based applications; for example, “Bravura” is intended for use by
scoring applications, and “Bravura Text” is intended for use by
text-based applications (or indeed for mixing musical symbols with free
text within a scoring application).

[^10]: The main problem concerns line spacing: because most applications determine the line spacing required for a font based on a sum of the ascender, descender and line gap values in the font (for which different applications on different operating systems use different combinations of the three places this can be defined, once the hhea table and twice in the OS/2 table), it is impractical to provide a font where all glyphs are scaled correctly relatively to one another in such a way that all musical symbols can be drawn at a single scale factor that complements text fonts at the same point size. Many applications clip glyphs that exceed the calculated line spacing, so in order to have a single font in which e.g. a G clef is drawn without clipping and an eighth note is drawn at a corresponding scale factor (such that the clef is around twice as tall as the note), the line spacing would have to be so tall that it would greatly distort the line spacing of the text. For more information about this issue, see [http://typophile.com/node/13081](media/image2.png). Bravura, for what it’s worth, uses very large line spacing (1.75 times its em square), such that 99% of glyphs are drawn without clipping in text-based applications, at the expense of making it practical to use the font mixed in-line with text.
