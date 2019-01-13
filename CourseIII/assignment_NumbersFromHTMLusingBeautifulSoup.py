#Scraping Numbers from HTML using BeautifulSoup In this assignment 
#you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. 
#The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.


#DATA FORMAT
#The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:

#<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
#<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
#<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

#You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers. 

import urllib.request
from bs4 import BeautifulSoup

data_url = "http://py4e-data.dr-chuck.net/comments_169959.html"

html = urllib.request.urlopen(data_url).read()
soup = BeautifulSoup(html,"html.parser")

tags = soup('span')

count = 0

for tag in tags:
	count += int(tag.contents[0])
	#print(tag.contents[0])
print(count)
