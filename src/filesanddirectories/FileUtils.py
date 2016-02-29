import os
import xml.etree.ElementTree as ET
"""
This script takes input input to list all files recursively
"""
reports = {}
rootDir = os.path.normpath("C:\\tmp\\reports\\billing-reports")

for r in os.listdir(rootDir):
    print(os.path.abspath(r))
# print(rootDir)
for root, dir, files in os.walk(rootDir):
    path = root.split('/')
    print (len(path) -1) *'----', os.path.basename(root)
    for file in files:
        reports[file]= os.path.abspath(file)
        print(len(path)*'----'),file, os.path.abspath(file)
#
# for reportPath in reports.values():
#     print "Processing {}".format(reportPath)
#     tree = ET.parse(reportPath)
#     root = tree.getroot()
#     root.findAll("[@name='qryPrompt_Bill Method']")


