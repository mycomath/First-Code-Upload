x = input("Enter in a value for x that is less than 10.\n")

while x < 10.0: 
	print x
	x = x + 1.0
	
if x >= 10:
	print "Can't you follow directions? :)"

###########################################################

print "I am a bot that helps you determine probability! Isn't this exciting?"

a = input("Enter the number of possibilities the first event has.")
b = input("Enter the number of possibilities the second event has.")

c = a**b

print "Congratulations, the total number of available possibilities is" + " " + str(c) 
print "Meanwhile, go suck an egg."