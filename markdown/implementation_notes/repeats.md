Scoring programs should draw their own repeat barlines using primitives
to draw the thick and thin lines and **repeatDots** to draw the dots, not
use the precomposed glyphs **repeatLeft** or **repeatRight**.

**dalSegno** and **daCapo** are provided for compatibility with the Unicode
Musical Symbols range. Scoring applications should allow the user to
specify the appearance of the *da capo* and *dal segno* instructions
using any regular text font.
