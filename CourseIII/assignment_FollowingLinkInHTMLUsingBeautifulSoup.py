#In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
#The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name
# in the list, follow that link and repeat the process a number of times and report the last name you find.

import urllib.request
from bs4 import BeautifulSoup

#Accodrding to the question.
data_url = "http://py4e-data.dr-chuck.net/known_by_Chu.html"
repetition = 7
linkPosition = 18
##
allLinks = list()
allNames = list()

for i in range(repetition):
	html = urllib.request.urlopen(data_url).read()
	soup = BeautifulSoup(html,"html.parser")
	tags = soup('a')
	for tag in tags:
		urls = tag.get('href',None)
		allLinks.append(urls)
		names = tag.text
		allNames.append(names)

	print(allLinks[linkPosition-1])
	print(allNames[linkPosition-1])
