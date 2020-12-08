Font-specific metadata locations
--------------------------------

SMuFL-compliant applications running on desktop operating systems such
as Windows, macOS, or Linux need to be able to determine whether a given
font installed on the system is itself SMuFL-compliant.

There is no simple way to encode this information in the font
itself[^15], so instead applications should identify SMuFL-compliant
fonts by the presence of the font-specific JSON metadata file in a known
location.

### System-wide location

It is recommended that, if possible, the font metadata is installed in a
system-wide location that allows access by all users on the system:

-   Windows: %COMMONPROGRAMFILES%/SMuFL/Fonts/*fontname*/*fontname*.json

-   macOS: /Library/Application
    Support/SMuFL/Fonts/*fontname*/*fontname*.json

-   Linux: $XDG_DATA_DIRS/SMuFL/Fonts/*fontname*/*fontname*.json

On Windows, the %COMMONPROGRAMFILES% environment variable expands to
C:\\Program Files\\Common Files, or its localised equivalent.

On Linux, $XDG_DATA_DIRS is an environment variable defined by the
[XDG Base Directory Specification](http://standards.freedesktop.org/basedir-spec/latest/).

It is typically necessary to require administrator privileges to install
files into these locations. However, it is also recommended that, if
possible, fonts themselves should also be installed in system-wide
locations, so if the metadata is installed by the same installer as the
fonts, no additional privileges will typically be required.

### User-specific location

If it is impossible or inappropriate to install the font metadata in a
system-wide location, use a user-specific location instead:

-   Windows: %LOCALAPPDATA%/SMuFL/Fonts/*fontname*/*fontname*.json

-   macOS: \~/Library/Application
    Support/SMuFL/Fonts/*fontname*/*fontname*.json

-   Linux: $XDG_DATA_HOME/SMuFL/Fonts/*fontname*/*fontname*.json

On Windows, %LOCALAPPDATA% expands to
C:\\Users\\*username*\\AppData\\Local.

On Linux, $XDG_DATA_HOME is an environment variable for user-specific configuration files,
defined by the [XDG Base Directory Specification](http://standards.freedesktop.org/basedir-spec/latest/).

On macOS, \~ is a shortcut to the current user's home folder,
e.g. /Users/*username*/.

It is not typically necessary to require administrator privileges to
install files into these locations. However, files installed in these
locations will not be accessible to any other user account on the
system.

### Private fonts

If a font is not designed to be used outside of a particular, specific
application, then of course it is not mandatory for it to be installed
in a system-wide location, nor for its metadata to be installed in these
publicly accessible locations: a private font intended for use within
the confines of a single application may choose to install its metadata
in any convenient private location.

### Precedence rules

Because font-specific metadata may be installed in either (or both) a
user-level location or a system-level location, applications should give
metadata found in the user-level location precedence over metadata found
in the system-level location.

[^15]: None of the existing tables in TrueType or OpenType fonts lend themselves to storing arbitrary data that could be used to identify a SMuFL-compliant font without subverting the purpose of an existing field in a table, which could have unforeseen side effects.
