#'''
#2.3 Write a program to prompt the user for hours and rate per
#hour using raw_input to compute gross pay.
#Use 35 hours and a rate of 2.75 per hour to test the program
#(the pay should be 96.25).
#'''

hrs = input("Enter hours:")
rate =input("Enter rate:")

pay = float(rate)*int(hrs)

print(pay)
