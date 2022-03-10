Recommended characters and optional glyphs
------------------------------------------

One of the aims of SMuFL is to make it as simple as possible for
developers both of fonts and of scoring software to implement support
for a wide range of musical symbols. Although modern font technologies
such as OpenType enable a great deal of sophistication in automatic
substitution features[^6], applications that wish to use SMuFL-compliant
fonts are not obliged to support advanced OpenType features.

The basic requirements for the use of SMuFL-compliant fonts are the
ability to access glyphs by their Unicode code point, to measure glyphs,
and to scale them (e.g. by drawing the font at different point sizes).
If applications are able to access OpenType features such as stylistic
sets and ligatures, then additional functionality may be enabled.

However, all glyphs that can be accessed via OpenType features are also
accessible via an explicit code point. For example, a stylistic
alternate for the sharp accidental designed to have a clearer appearance
when reproduced at a small size can be accessed as a stylistic alternate
for accidentalSharp, but also by way of its explicit code point, which
will be in the range U+F400–U+F8FF.

Because optional glyphs for ligatures, stylistic alternates, etc. are
not required, and different font developers may choose to provide
different sets (e.g. several different appearances of tab clefs, or
different sets of glyphs whose designs are optimized for drawing at
different optical sizes), SMuFL does not make any specific
recommendations for how these glyphs should be assigned explicit code
points, except that they must be within the range U+F400–U+F8FF, which
is reserved for this purpose and for any other private use required by
font or application developers.

In summary, recommended characters are encoded from U+E000, with a
nominal upper limit of U+F3FF (a total of 5120 possible characters),
while optional glyphs (ligatures, stylistic alternates, etc.) are
encoded from U+F400, with a nominal upper limit of U+F8FF (a total of
1280 possible glyphs).

In order for a font to be considered SMuFL-compliant, it should
implement as many of the recommended characters as are appropriate for
the intended use of the font, at the specified code points. Fonts need
not implement every recommended character, and need not implement any
optional glyphs, in order to be considered SMuFL-compliant.

[^6]: See https://www.adobe.com/devnet/opentype/afdko/topic_feature_file_syntax.html
