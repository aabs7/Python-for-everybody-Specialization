# Write a program that prompts for a file name, then opens that file and reads through the file, 
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the 
# average of those values and produce an output as shown below.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are 
# testing below enter mbox-short.txt as the file name.
# Average spam confidence: 0.750718518519

file = input("Enter the file name:")
fHandle = open(file)
count = 0
sum = 0

for line in fHandle:
	if not line.startswith("X-DSPAM-Confidence:"): continue
	pos = line.find("0")
	sum += float(line[pos:])
	count += 1

average = sum / count
print("Average spam confidence = ",average)


