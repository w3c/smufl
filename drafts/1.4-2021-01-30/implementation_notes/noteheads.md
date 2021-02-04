These noteheads should be combined with stems and flags as necessary to
create complete notes. In text-based applications, per the Unicode
Musical Symbols documentation:

![](../media/precomposed-notes-unicode.png)

Scoring applications should draw stems using primitives, rather than
using stem (i.e. U+1D165 as shown in the above image[^1]), so that they
can be drawn to the correct length.

*See also* the implementation notes for flags.

[^1]: From Chapter 15 “Symbols”, *The Unicode Standard, Version 6.2*. Ed. Julie D. Allen et al. Mountain View; The Unicode Consortium, 2012.
