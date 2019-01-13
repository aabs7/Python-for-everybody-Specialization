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

for i in range(repetition):
	html = urllib.request.urlopen(data_url).read()
	soup = BeautifulSoup(html,"html.parser")
	tags = soup.find_all('a')

	#find the link at linkPosition
	positionLink = tags[linkPosition-1]

	next_data_url = positionLink.get('href',None)

	#next url is opening the url which is at linkPosition
	data_url = next_data_url
	print(next_data_url)

