#!/usr/bin/python3
import os
import pathlib
import sys

"""
Grabs file in directory and changes the name to the parent directory + its original extension.

./test/alskdjflkasdjf.gif -> test.gif
./test5/a98123lfadsf.gif -> test5.gif
./another-one/mlcnvkasu.jpg -> another-one.jpg

Usage:
python3 scripts/convert.py [target directory]
"""

files = pathlib.Path(sys.argv[1]).glob('**/*')

for emoji in files:
    if emoji.suffix not in {".gif", ".png", ".jpg"}:
        continue

    # urllib.parse.unquote - we can't because UTF8 path issues :c
    file = str(emoji.parent) + str(emoji.suffix)
    fqpn = emoji.resolve()

    print("Renamed %s to %s" % (fqpn, file))
    os.rename(emoji.resolve(), file)
