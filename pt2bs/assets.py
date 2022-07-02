programmsg: str = "\n PT2BS - Python to binary build system based on nuitka\n"
helpmsg: str = "   -g, --generate | generate new build.py file with options by args\n   -h, --help     | print this message\n   -v, --version  | print program version\n"
main_file: str = "\n Main file of program."
o_file: str = "\n Output file."
cmassage: str = "\n [build.py generated]\n"
build_py: str = '''#!/usr/bin/env python3

from os import chdir, mkdir
from os import system as sh
from os.path import isdir
from sys import argv

# main file in program
MAIN: str = "%s"

# output file
OFILE: str = "%s"

# flags for python interpreter
PYFLAGS: str = """ \\
    -OO \\
"""

# compile flags
CFLAGS: str = """ \\
    --warn-implicit-exceptions \\
    --warn-unusual-code \\
    --follow-imports \\
    --python-flag=-OO \\
    --disable-ccache \\
    --lto=yes \\
"""

# dir for binary file
BINDIR: str = "/usr/local/bin"

# build command
BUILD: str = f"python {PYFLAGS} -m nuitka {CFLAGS} -o {OFILE} ../{MAIN}"

# if no flags
if len(argv) == 1:
    print("incorrect flags")

# build option
elif argv[1] == "build":
    if isdir("build/"):
        chdir("build/")

    else:
        mkdir("build/")
        chdir("build/")

    sh(BUILD)

# install option
elif argv[1] == "install":
    if isdir("build/"):
        chdir("build/")

    else:
        mkdir("build/")
        chdir("build/")

    sh(BUILD)

    # move file in BINDIR
    sh(f"sudo mv {OFILE} {BINDIR}")

else:
    print("incorrect flags")
'''
version: str = "pt2bs - 0.1"
empty_field: str = "\n [input field is empty]\n"
io_error: str = "\n [file inaccessible]\n"
