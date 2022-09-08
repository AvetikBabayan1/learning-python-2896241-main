#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    # make a duplicate of an existing file
    if path.exists("bakkara.txt.bak"):
        # get the path to the file in the current directory
        source = path.realpath("bakkara.txt.bak")
        # let's make a backup copy by appending "bak" to the name
        dst = source + ".bak"
        shutil.copy(source, dst)

        # rename the original file
        #os.rename("bakkara.txt", "new-bakkara.txt")
        # now put things into a ZIP archive
        #d, tail =path.split(source)
        #shutil.make_archive("archieve", "zip", d)
        # more fine-grained control over ZIP files
        with ZipFile("test.zip", "w") as newzip:
            newzip.write("bakkara.txt.bak")
            newzip.write("bakkara.txt.bak.bak")
            newzip.write("new-bakkara.txt")
      
if __name__ == "__main__":
    main()
