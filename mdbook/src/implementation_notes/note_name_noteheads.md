These noteheads are designed for use by scoring applications to render
music where the names of notes are shown inside noteheads. For practical
use, scoring applications should provide a means of automatically
substituting regular noteheads for the appropriate note name notehead
glyph according to the pitch of each note.

For maximum legibility, stave lines and ledger lines should not be drawn
through the letterforms in these noteheads. Applications should either
draw segments of stave lines and ledger lines to the left and right of
the extent of each notehead positioned on a line, or draw
**noteEmptyWhole**, **noteEmptyHalf** and **noteEmptyBlack** as appropriate
in white (or the paper color) on top of the stave or ledger line but behind
the note name notehead.

*See also* the implementation notes for **Noteheads**.
