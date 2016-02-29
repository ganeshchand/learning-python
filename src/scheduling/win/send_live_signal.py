import os
import time
from os.path import expanduser

userHomeDir = expanduser("~")
logDir = userHomeDir + """\\temp1111"""
if not os.path.exists(logDir):
    print(logDir + " doesn't exist. Creating...")
    # os.makedirs(logDir)
    os.mkdir(logDir)
livelog = open(logDir+"\\live.log", "at")
os.listdir(logDir)

message = time.strftime("System is alive at %Y-%m-%dT%H:%M%S\n", time.localtime())

livelog.write(message)
livelog.close()
