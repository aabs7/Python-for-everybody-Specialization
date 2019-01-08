#5.2 Write a program that repeatedly prompts a user for integer numbers until the
#user enters 'done'. Once 'done' is entered, print out the largest and smallest of
#the numbers. If the user enters anything other than a valid number catch it with
#a try/except and put out an appropriate message and ignore the number. Enter the
#numbers from the book for problem 5.1 and Match the desired output as shown.

largest = None
smallest = None

while True:
	#below statement checks if only number is entered
	try:
		number = input("Enter a number: ")
		if number == "done":	break
		n = int(number)
		if largest == None or largest < n:
			largest = n
		if smallest == None or smallest > n:
			smallest = n
	#if other than number is entered
	except:
		print ("Invalid Input")

print("Largest Number is: ",largest)
print("Smallest Number is: ",smallest)
