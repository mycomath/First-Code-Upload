print "\nWelcome to Old-Mart. We have a fine selection of video games."
ans = True
while ans:
	print ("""
	1. Zelda - 10.00$
	2. Sonic - 8.99$
	3. Mario - 15.00$
	4. Asteroids - 2.00$
	5. Exit Menu
	""")
	ans = raw_input("Which game would you like to purchase? ")
	if ans == "1":
		print "You are purchasing Zelda."
		m = input("Please provide payment for your selection. ")
		a = m - 10.00
		print "Your change is " + str (a) + "$" + " thank you for shopping at Old-Mart."
		
	elif ans == "2":
		print "You are purchasing Sonic."
		m = input("Please provide payment for your selection. ")
		a = m - 8.99
		print "Your change is " + str (a) + "$" + " thank you for shopping at Old-Mart."
		
	elif ans == "3":
		print "You are purchasing Mario."
		m = input("Please provide payment for your selection. ")
		a = m - 15.00
		print "Your change is " + str (a) + "$" + " thank you for shopping at Old-Mart."
		
	elif ans == "4":
		print "You are purchasing Asteroids."
		m = input("Please provide payment for your selection. ")
		a = m - 2.00
		print "Your change is " + str (a) + "$" + " thank you for shopping at Old-Mart."
		
	elif ans == "5":
		print "Please come back later!"
		ans = None

	else:
		print ("\nNot a valid selection, please try again.")