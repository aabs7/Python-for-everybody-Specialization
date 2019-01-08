
#"""
# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by
#hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then
#splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown below.
#Note that the autograder does not have support for the sorted() function.
#"""

#output:
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1

file = input("Enter file:")
fHandle = open(file)
count = dict()

for line in fHandle:
	if line.startswith("From "):
		#extract just hours
		hour = line.split()[5].split(':')[0]
		#count for each hours in which email has arrived
		count[hour] = count.get(hour,0) + 1

#dict.items() return 'list' of tuples
#for eg: dict = {'Name':'zara','Age':7}
#	 print (dict.items())
#returns [('Age',7),('Name','Zara')]

for key,value in sorted(count.items()):
	print(key,value)



