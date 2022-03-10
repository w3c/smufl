The position _y_ = 0 corresponds to a staff line for each rest glyph, but it is not necessarily the same staff line for every glyph in this range: for example, **restWhole** hangs from the nominal staff line at _y_ = 0, while **restHalf** sits on the nominal staff line at _y_ = 0.

Scoring applications should draw multiple measure rests using primitives to provide variable width and line thickness rather than using **restHBar**.

“Old style” multiple measure rests can be created by laying out **restLonga** (four bars), **restDoubleWhole** (two bars) and **restWhole** (one bar) next to each other.

For dotted rests, the augmentation dot glyph **augmentationDot** should be used.
