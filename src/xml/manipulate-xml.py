import xml.etree.ElementTree as ET



# load and parse xml document

tree = ET.ElementTree(file="/Users/ganeshchand/gh/gc/python/learning-python/src/xml/report.xml")

# root element

root = tree.getroot()

print(root.toString)

# Accessing attributes

root.tag, root.attrib

# You can iterate over root accessing it children

for child_of_root in root:
    print child_of_root.tag, child_of_root.attrib

# We can also access a specific child, by index:

root[0].tag, root[0].text

# total child elements of root
len(root)


# Finding interesting elements

# let's find all data elements and print name

for elem in root.iter('dataItem'):
    print(elem.text)




