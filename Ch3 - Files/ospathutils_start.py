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
    #print (os.name, os.path, os.curdir, os.environ) #getting and printing different OS attributes
    #print("Item exists: ", str(path.exists("textfile.txt"))) #checking, if certain named file exists, it path exists and boolean value, if so
    #print(str(path.isdir("C:/Users/Avetik/Downloads/learning-python-2896241-main/Ch3 - Files/"))) #checking, if the argument in function is a folder
    #print("Item is a file: ", str(path.isfile("bakkara.txt"))) #checking, if the argument is a file
    #print("Full path: ", path.realpath("challenge_solution.py")) #checking the full path to the file named as argument
    #print("File name is: ", path.split(path.realpath("challenge_solution.py"))) #get the name of the file with providing previous function as argument
    #t = time.ctime(path.getmtime("textfile.txt")) #variable which will keep in default time format the modification time of a given file
    #print("File last change at: ", t) #printing the time in a normal format
    #print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))#same as previous steps, but differently
    #checking how long ago file was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print(td)
if __name__ == "__main__":
    main()
