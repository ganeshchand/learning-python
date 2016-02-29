# Exercise 13 - Parameters, Unpacking and Variables

# Simple Script that accepts command line arguments and initailzied variables
# argv is used when you give input to the scirpts on the command line.
# raw_input() is used when you want users to input interactively as part of the runn#ing program

from sys import argv

script, first, second, third = argv
name = raw_input("What's your name?:")
print "\nWelcome {}!".format(name)
print "The script is called:", script
print "The value of first is:", first
print "The value of second is:", second
print "The value of third is:", third
