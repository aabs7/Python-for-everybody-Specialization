#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
#The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_169961.xml (Sum ends with 15)

#The data consists of a number of names and comment counts in XML as follows:

#<comment>
#  <name>Matthias</name>
#  <count>97</count>
#</comment>

#You are to look through all the <comment> tags and find the <count> values sum the numbers.
#The closest sample code that shows how to parse XML is geoxml.py.
#But since the nesting of the elements in our data is different than the data we are parsing in that sample code you will have to make real changes to the code.

#To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:

#counts = tree.findall('.//count')

import urllib.request
import xml.etree.ElementTree as ET

url = "http://py4e-data.dr-chuck.net/comments_169961.xml"
data = urllib.request.urlopen(url).read()

stuff = ET.fromstring(data)

lst = stuff.findall('comments/comment')
totalSum = 0
for item in lst:
	totalSum += int(item.find('count').text)

print(totalSum)
