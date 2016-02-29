# Exercise 15 - Reading Files

# Accept file name as part of script argument and read and print file contents

from sys import argv

script, fileName = argv
print "Input file to read {}\n".format(fileName)
# Modern way - auto closes


def readFile(fileName):

    """Reads a given file and prints each line
    """

    with open(fileName, 'rb') as f:
        for line in f:
            print line,
        lines = f.readlines()
        print len(lines)
readFile(fileName)    
while True:
    choice = raw_input("Do you want to read another file?:")
    if choice in ("YES", "Y", "y", "yes"):
        fileName = raw_input("Enter the file name to read:")
        readFile(fileName)
    elif choice in ("NO","no","No","n","N"):
        break
    else:
        print "Invalid choice. Good Bye!"
        break 

# Old way or reading a file. Requires closing the file object.
# f = open(fileName)
# print(f.read())
# f.close()
