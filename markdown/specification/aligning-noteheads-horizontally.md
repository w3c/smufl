Aligning noteheads horizontally
-------------------------------

The noteheadOrigin point is defined for noteheads with non-zero
left-hand side bearings, such as the double whole (breve) notehead that
has two vertical lines at either side of the oval notehead itself, as
illustrated in the figure below:

![](../media/notehead-origins.svg)

-   The horizontal grey lines denote staff lines, for scale.

-   The light blue boxes show glyph bounding boxes, with the left-hand
    side of the box corresponding to x=0.

-   The vertical dashed grey lines denote the left-hand edge of the
    rhythmic position, i.e. the position against which the notehead
    is aligned.

-   The red box shows the location of the noteheadOrigin point, as
    specified in the font metadata JSON file.

The left-hand example shows the alignment that will be produced simply
by positioning notehead glyphs using the left-hand edges of their
bounding boxes. The right-hand example shows the superior alignment that
can be produced by offsetting the double whole (breve) note leftwards by
the distance between x=0 and the noteheadOrigin point.
