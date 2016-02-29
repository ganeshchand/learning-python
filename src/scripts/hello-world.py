import os
print("Hello, World!")
print(os.getcwd())

# get current directory name
currDirPath = os.getcwd()
currDirPathNames = currDirPath.split("\\")
n = len(currDirPathNames)
currDirName = currDirPathNames[n-1]
print(currDirName)

