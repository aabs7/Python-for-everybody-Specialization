#"""
#9.4 Write a program to read through the mbox-short.txt and figure out who has the most commits. 
#The program looks for 'From ' lines and takes the second word of those lines as the person
# who sent the mail. The program creates a Python dictionary that maps the senders mail address 
#to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum 
#loop to find the most prolific committer.
#"""

#output
#cwen@iupui.edu 5

file = input("Enter file:")
fHandle = open(file)

count = dict()

for line in fHandle:
	if line.startswith('From '):
		word = line.split()
		#dict.get(key,default = None)
		#key- This is the key to be searched in dictionary.
		#default - This is the value to be returned in case the key doesnot exist.
		count[word[1]] =count.get(word[1],0) + 1
largest = 0
email = ''

for key in count:
	if count[key] > largest:
		largest = count[key]
		email = key

print (email,largest)


