#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    print(os.name)
    
    # Check for item existence and type
    print("Item exists ", str(path.exists("bakkara.txt")))
    print("It is a file : ", path.isfile("bakkara.txt"))
    print("It is a folder : ", path.isdir("bakkara.txt"))
    
    # Work with file paths
    print(path.realpath("bakkara.txt"))
    print(path.split(path.realpath("bakkara.txt")))
    
    # Get the modification time
    d=path.getmtime("bakkara.txt")
    print(time.ctime(d))
    print(datetime.datetime.fromtimestamp(d))
    
    # Calculate how long ago the item was modified
    td = datetime.datetime.now()-datetime.datetime.fromtimestamp(d)
    print (td)
    print (td.total_seconds())
if __name__ == "__main__":
    main()
