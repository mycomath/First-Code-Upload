#def converttemp(temp, unit):
#	if unit == 'F':
#		newtemp = (temp - 32) * 5/9
#		stringnewtemp = string(newtemp)
#		print "Your converted temperature is " + stringnewtemp + " unit"
#	elif unit == "C":
#		newtemp = (temp * 9/5) + 32
#		stringnewtemp = string(newtemp)
#		print "Your converted temperature is " + stringnewtemp + " unit"
#		
#def main():
#	while True:
#		unit = input ("Which temperature are you converting from? (C/F)")
#		temp = float(input("Enter your temperature value."))
#		return converttemp(temp, unit)
#		quit = raw_input("Do another conversion? (Y/N)")
#		if quit == "N":
#			break
#		elif quit == "Y":
#
#			main()
#
#def main():
#	while True:
#		a = raw_input("Are you starting with Celsius or Fahrenheit? (C/F) ").lower().strip()
#	return tempcon()
#		quit = raw_input("Do you want to convert another temperature?")
#		if quit == "No":
#			break
#		elif quit == "Yes":
#			main()
#main()

def tempcon():
	if a == "c":
		print "Your original value is in degrees Celcius."
		m = (b*(9.0/5.0)+32.0)
		print "The converted value is " + str(m) + " degrees Fahrenheit."
	if a == "f":
		print "Your original value is in degrees Fahrenheit."
		m = ((b-32.0)*(5.0/9.0))
		print "The converted value is " + str(m) + " degrees Celsius."

def variable():
	global a
	global b
	a = raw_input("Are you starting with Celsius or Fahrenheit? (C/F) ").lower().strip()
	b = float(input("What is your initial value? "))
	tempcon()
	quit = raw_input("Do another conversion?").lower()
	if quit == "yes":
		variable()
	else:
		print "Thanks, see you soon."
		
variable()