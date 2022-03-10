Scoring applications may choose to create e.g. *ottava alta* and *ottava
bassa* versions of the G clef and F clef by combining **gClef** and **fClef**
with **clef8** and **clef15** rather than using the precomposed glyphs.

The basic G clef, F clef and C clef symbols can be positioned at
different vertical positions relative to the staff as required (e.g. the
C clef can be positioned to create an alto or tenor clef).

Clef changes are normally drawn at two-thirds the size of clefs at the
beginning of the system[^1], but different publishers and engravers may
prefer to use a different size. Dedicated glyphs for drawing a clef
change are provided for the three most commonly-used clefs (**gClefChange**,
**cClefChange**, and **fClefChange**), together with a combining control
character (**clefChangeCombining**) that font designers may use to produce
smaller versions of less commonly-used clefs by way of glyph
substitution (such as OpenType ligatures). Scoring applications may
choose to use these dedicated clef change glyphs if they do not provide
the end user with control over the size of clef changes. Otherwise,
scoring applications should draw clef changes by using the regular clef
glyphs at a smaller point size, either fixed at two-thirds the size of
normal clefs, or at a size of the end user’s choosing.

[^1]: Gould, *ibid.*, page 7.
