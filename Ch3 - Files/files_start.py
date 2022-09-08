#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():
    """""
     #open a file
     myfile=open('textfile.txt', "w+")

     # append changes to a file
     myfile = open('textfile.txt', "a+")
     # add some content to a file
     for i in range (10,20):
         myfile.write("The line number "+ str(i) +"\n" )
    """
    #open file for reading
    myfile=open('textfile.txt', "r")
    #check, if file is in a correct mode
    if myfile.mode=='r':
        #   content = myfile.read() #read a content of the file and after print it
        #   print(content)
        """ #close the file after iteraction (not required, if no changes applied to it)
        myfile.close()
        Now reading the file line by line as string
        """
        fileline=myfile.readlines()
        for x in fileline:
            print(x)

if __name__ == "__main__":
    main()
