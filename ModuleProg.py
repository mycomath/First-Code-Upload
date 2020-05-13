import sys
import time

def CheckDate(a):
	if a.isdigit():
		if a == 0:
			print "Today is Sunday."
		if a == 1:
			print "Today is Monday."
		if a == 2:
			print "Today is Tuesday."
		if a == 3:
			print "Today is Wednesday."
		if a == 4:
			print "Today is Thursday."
		if a == 5:
			print "Today is Friday."
		if a == 6:
			print "Today is Saturday."
				
	elif a.isalpha():
		if a == "sun":
			print "Today is Sunday."
		if a == "mon":
			print "Today is Monday."
		if a == "tue":
			print "Today is Tuesday."
		if a == "wed":
			print "Today is Wednesday."
		if a == "thu":
			print "Today is Thursday."
		if a == "fri":
			print "Today is Friday."
		if a == "sat":
			print "Today is Saturday."
			
	else:
		print "There is nothing else to do."
		
def main():
	a = raw_input("Enter a number 0-6 or the first three letters of a day of the week.").lower
	CheckDate(a)
	
main()