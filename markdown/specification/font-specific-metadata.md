Metadata for SMuFL-compliant fonts
----------------------------------

To help software developers integrate SMuFL-compliant fonts, it is
recommended that font designers provide a font-specific metadata file,
in JSON format, in the distribution package for their fonts.

The metadata file allows the designer to provide information that cannot
easily (or in some cases at all) be encoded within or retrieved from the
font software itself, including recommendations for how to draw the
elements of music notation not provided directly by the font itself
(such as staff lines, barlines, hairpins, etc.) in a manner
complementary to the design of the font, and important glyph-specific
metrics, such as the precise coordinates at which a stem should connect
to a notehead.

Glyph names may be supplied either using their Unicode code point or
their canonical glyph name (as defined in the glyphnames.json file – see
above). Measurements are specified in staff spaces, using floating point
numbers to any desired level of precision.

The following key/value pairs are mandatory:

| *Key name*      | *Description*
| --------------- | ----------------------------------------------------
| "fontName"      | The name of the font to which the metadata applies
| "fontVersion"   | The version number of the font to which the metadata applies

All other key/value pairs are optional.
