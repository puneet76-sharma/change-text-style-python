# pip install colorama
# pip install termcolor
# pip install pyfiglet

import sys

from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected

word=str(input("Enter text for change text style: "))
cprint(figlet_format(word, font='standard'), 'yellow', 'on_cyan', attrs=['bold'])

input()