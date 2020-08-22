# pip install colorama
# pip install termcolor
# pip install pyfiglet

# change-text-style-python
Makes ANSI escape character sequences (for producing colored terminal text and cursor positioning) work under MS Windows.

ANSI escape character sequences have long been used to produce colored terminal text and cursor positioning on Unix and Macs. Colorama makes this work on Windows, too, by wrapping stdout, stripping ANSI sequences it finds (which would appear as gobbledygook in the output), and converting them into the appropriate win32 calls to modify the state of the terminal. On other platforms, Colorama does nothing.

Colorama also provides some shortcuts to help generate ANSI sequences but works fine in conjunction with any other ANSI sequence generation library, such as the venerable Termcolor (https://pypi.org/project/termcolor/) or the fabulous Blessings (https://pypi.org/project/blessings/).

This has the upshot of providing a simple cross-platform API for printing colored terminal text from Python, and has the happy side-effect that existing applications or libraries which use ANSI sequences to produce colored output on Linux or Macs can now also work on Windows, simply by calling colorama.init().

# Usage
# Initialisation

Applications should initialise Colorama using:

from colorama import init
init()

pyfiglet is a full port of FIGlet (http://www.figlet.org/) into pure
python. It takes ASCII text and renders it in ASCII art fonts (like
the title above, which is the 'block' font).
