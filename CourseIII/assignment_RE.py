#Finding Numbers in a Haystack

#In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers. 

import re

file = input("Enter file name:")
fHandle = open(file)

ts = 0
count = 0

for line in fHandle:
	f = re.findall('[0-9]+',line)
	for num in f:
		if num != []:
			count = count + 1
			ts = ts + int(num)

print("There are",count,"values with a sum=",ts)



