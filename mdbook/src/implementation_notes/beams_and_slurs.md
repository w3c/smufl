These are format characters as defined in the Unicode Standard:[^1]

> Extensive ligature-like beams are used frequently in musical notation
> between groups of notes having short values. The practice is widespread
> and very predictable, so it is therefore amenable to algorithmic
> handling. The format characters U+1D173 MUSICAL SYMBOL BEGIN BEAM and
> U+1D174 MUSICAL SYMBOL END BEAM can be used to indicate the extents of
> beam groupings. In some exceptional cases, beams are left unclosed on
> one end. This status can be indicated with a U+1D159 MUSICAL SYMBOL NULL
> NOTEHEAD character if no stem is to appear at the end of the beam.
>
> Similarly, format characters have been provided for other connecting
> structures. The characters U+1D175 MUSICAL SYMBOL BEGIN TIE, U+1D176
> MUSICAL SYMBOL END TIE, U+1D177 MUSICAL SYMBOL BEGIN SLUR, U+1D178
> MUSICAL SYMBOL END SLUR, U+1D179 MUSICAL SYMBOL BEGIN PHRASE, and
> U+1D17A MUSICAL SYMBOL END PHRASE indicate the extent of these features.
> Like beaming, these features are easily handled in an algorithmic
> fashion.
>
> These pairs of characters modify the layout and grouping of notes and
> phrases in full musical notation. When musical examples are written or
> rendered in plain text without special software, the start/end format
> characters may be rendered as brackets or left uninterpreted. To the
> extent possible, more sophisticated software that renders musical
> examples inline with natural-language text might interpret them in their
> actual format control capacity, rendering slurs, beams, and so forth, as
> appropriate.

Scoring applications may choose to implement these format characters for
beams, slurs, phrase marks and ties or not, as they wish.

[^1]: *Ibid.*, Allen, page 537.
