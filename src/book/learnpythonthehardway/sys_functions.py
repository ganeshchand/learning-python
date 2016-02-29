# Using Sys Module

from sys import argv
from sys import path
from sys import modules

scriptName = argv[0]
scriptDirectory = path[0]
print "Script Name - argv[0]: {}".format(scriptName)
print "script Directory - path[0]: {}".format(scriptDirectory)
print "Modules used in the script:\n"

for module in modules.items():
    print "module Name: {}".format(module)



