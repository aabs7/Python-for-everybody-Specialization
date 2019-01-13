#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file and enter the sum below:

#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_169962.json (Sum ends with 64)

#Data Format

#The data consists of a number of names and comment counts in JSON as follows:

#{
#  comments: [
#    {
#      name: "Matthias"
#      count: 97
#    },
#    {
#      name: "Geomer"
#      count: 97
#    }
#    ...
#  ]
#}

import urllib.request
import json

url = "http://py4e-data.dr-chuck.net/comments_169962.json"

data = urllib.request.urlopen(url).read()
info = json.loads(data)
#print(info)
totalSum = 0
for i in info['comments']:
	totalSum +=int(i['count'])
print(totalSum)
