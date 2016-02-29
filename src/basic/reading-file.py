# input file
filePath = "/etc/passwd"


# read a file
def inputFile(inputfilePath):
    return inputfilePath


def transformInput():
    with open(inputFile(filePath), 'r') as inFile:
        names = []
        for line in inFile:
            name = line.strip().split(':')[0]  # we want the user names only.
            if not name.startswith("#"):  # ignore comments
                names.append(name)
    return names

def filterNames():
    requiredNames = []
    for name in transformInput():
        if not name.startswith("_"):
            requiredNames.append(name)
    return requiredNames


def aggregateName():
    count = len(filterNames())
    return count
    #print("total count: {}".format(count))

def saveAggregateResult():

    # save in a text file

    outputDir = "/tmp/python/output"
    filename = "name-count.txt"

    import os

    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    outputFilePath = outputDir + os.sep + filename

    with open(outputFilePath, 'w') as oFile:
        oFile.write("Name Count: {}\n".format(str(aggregateName())))

# transformInput()
# readInputFile(filePath)
# filterNames()
#aggregateName()
saveAggregateResult()
