from BeautifulSoup import BeautifulSoup as Soup
import urllib2

file = "/Users/ganeshchand/gh/gc/python/learning-python/src/xml/report.xml"

fileReader = open(file,'rb')
soup = Soup(fileReader)
# print soup


for dataitem in soup.findAll('dataitem'):
    dataitem_attrs = dict(dataitem.attrs)
    expression = dataitem.find('expression')
    expression_attrs = dict(expression.attrs)
    print dataitem_attrs
    print expression_attrs

for expression in soup.findAll('dataitem'):

    print expression.contents[1].text