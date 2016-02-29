import logging
import os
from os.path import expanduser

logging.warning('This is a Warning') # Prints a message to the console
logging.info('This is just an FYI')  # Doesn't print. Default warning level is Warning.


# Logging to a File

logDir = os.path.join(expanduser("~"), 'templog')
if not os.path.exists(logDir):
    os.makedirs(logDir)
print(logDir)
logFile = 'python-log.log'
logFilePath = os.path.join(logDir + logFile)

logging.basicConfig(filename='test.log', filemode='a', level=logging.DEBUG)
# print(os.path.isfile(logFilePath))
logging.debug("This message should to the the log file")
logging.info('So should this')
logging.warning("And this, too")






