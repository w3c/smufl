This range of Kievan square notation glyphs are encoded in Unicode from
version 8.0 at the code points [U+1D1DE–U+1D1E8](https://www.unicode.org/charts/PDF/U1D100.pdf).

For **kievanNoteWholeFinal** and **kievanNoteReciting**, the symbol is
positioned on the staff such that for a note on a staff line, the staff
line passes between the two thick horizontal lines. For **kievanNoteWhole**
on a staff line, the staff line passes between the two diamonds. For
**kievanNote8thStemDown** on a staff line, the staff line passes through the
top diamond.

In the type of Kievan notation used in modern chant books of the Russian
Orthodox Church, the symbol for half note has two variants: the variant
with the long tail down (**kievanNoteHalfStemDown**) is used when the note
occurs on a staff line, and the variant with the long tail up
(**kievanNoteHalfStemUp**) is used when the note occurs in a space. Only the
first of these characters is encoded in Unicode, while the second
character is to be selected programmatically via font features; SMuFL
encodes both characters at separate code points.

Kievan notes may be beamed, with stems up or stems down. These ligatures
are not encoded explicitly either in Unicode or in SMuFL, but it is
recommended that fonts provide ligatures. They may also be available in
Unicode fonts via ligature substitution by entering, e.g., the following
character sequence: **U+1D1E4 Musical Symbol Kievan Quarter Note Stem
Down**, **U+1D173 Musical Symbol Begin Beam**, **U+1D1E4 Musical Symbol Kievan
Quarter Note Stem Down**, **U+1D174 Musical Symbol End Beam**.
