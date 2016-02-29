import os
import tempfile


def sayHello():
    print("hello Python")
    print(tempfile.gettempdir())
    # f = tempfile.TemporaryFile()
    outputFile = tempfile.gettempdir() + os.path.sep + "number_up_to_10.txt"
    print(outputFile)


if __name__ == '__main__':
    sayHello()
