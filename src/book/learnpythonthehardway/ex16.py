# Exercise 16 - Reading and Writing Files

"""
Common methods for file objects:
 close() - Closes the file.
 read() - read the contents of the file. You can assign the result to a variable
 readline - reads just one line of a text file.
 truncate - empties the file. 
 write(stuff) - writes stuff to the file.
"""

from sys import argv
from os import linesep


script, filename = argv

print "We're going to erase %s file in order to write into it." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want to proceed, hit RETURN."

raw_input("?")

print "Opening the file..."

outputFile = open(filename, 'wb')

print "Truncating the file..existing content will be wiped out!."

outputFile.truncate()

print "Now I'm going to ask you for three lines to write to the file."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "Now writing the above lines into the file..."

outputFile.write(line1)
outputFile.write(linesep)
outputFile.write(line2)
outputFile.write(linesep)
outputFile.write(line3)
outputFile.write(linesep)
outputFile.write("{}{}{}{}{}{}".format(line1,linesep,line2,linesep,line3,linesep))

print "Finished writing. Now closing the file."

outputFile.close()

