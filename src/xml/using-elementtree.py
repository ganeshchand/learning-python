# Python XML parsing using ElementTree
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

# Parsing XML from String

xmlString = """<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>"""

# Extract root
# fromstring parses XML from a string directly into an Element, which is the root element
# of the parsed tree.
root = ET.fromstring(xmlString)  # root is an Element. It has a tag and dictionary of attributes
print "root node is {}".format(root.tag)
print "root node has {} child nodes".format(len(root))

# print "root attributes {}".format(root.attrib)


# iterating over children

for child in root.iter():
    print "{}: {}".format(child.tag, child.text)  # prints the node name

for neighbor in root.iter('neighbor'):
    print neighbor.attrib

# Element.findall() finds only elements with a tag which are direct children of the current element.
# Element.find() finds the first child with a particular tag, and Element.text accesses the element’s text content.
# Element.get() accesses the element’s attributes


print "Displaying Country with a rank > 50"
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        print country.attrib['name']  # country.attrib is a dictionary of type {'name': 'value'}

# Parsing XML with Namespaces

reportWithNamespace = "/Users/ganeshchand/gh/gc/python/learning-python/src/xml/report.xml"
report = "/Users/ganeshchand/gh/gc/python/learning-python/src/xml/report-without-namespace.xml"

tree = ET.parse(report)  # parse returns XML Tree

print tree

reportRoot = tree.getroot()

print reportRoot.tag
print reportRoot.attrib

for child in root.findall('modelPath'):
    print child.tag
