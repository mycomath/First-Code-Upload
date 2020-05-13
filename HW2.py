# 
# Author       : Andrew Caudill
# Date         : 2018.02.06
# Version      : 0.0.1
# Email        : acaudill5@radford.edu
# Assignment   : Lab 02
# Description  : Source code for Lab 02.
# 
##############################################################################

print "Temperature Converter.\n"

def tempcon(a,b):
# This is my converter function which gets parsed the unit and temp value to convert.
	if a == "c":
		print "Your original value is in degrees Celcius."
		m = (b*(9.0/5.0)+32.0)
		print "The converted value is " + str(m) + " degrees Fahrenheit."
# This if-statement covers Celsius, and converts C to F then prints the converted F value.
	if a == "f":
		print "Your original value is in degrees Fahrenheit."
		m = ((b-32.0)*(5.0/9.0))
		print "The converted value is " + str(m) + " degrees Celsius."
# This if-statement is the compliment to the previous.

def variable():
# This is my main function where I prompt the user for their input.
	a = raw_input("Are you starting with Celsius or Fahrenheit? (C/F) ").lower().strip()
	b = float(input("What is your initial value? "))
# These lines allow the user to input the initial temperature type and the value.
	tempcon(a,b)
# This line parses the previously mentioned values into the converter function.
	quit = raw_input("Do another conversion? (yes or no) ").lower().strip()
	if quit == "yes":
		variable()
	else:
		print "Thanks for using the temperature converter."
# This line allows the user to quickly convert another value by entering yes.
		
variable()
# I initially struggled with global variable name until I learned the parse technique.
# I can also leave the variable global by putting the keyword; however, this is a security risk. 

#################################### Game Sale Interface ###################

print "Video Game Interface.\n"

# For the video game sale, I wanted to have a menu that interfaces with the user.
# To accomplish this I print a body of text explaining the price and game each tied to a numerical value.

def gamemenu():
# Heres my function for the game menu.
	ans = True
	while ans:
# I included a simple while command to create an infinite loop to keep the menu up.
		print ("""
	1. Zelda - 10.00$
	2. Sonic - 8.99$
	3. Mario - 15.00$
	4. Asteroids - 2.00$
	5. Exit Menu
	""")
# This the menu the user is displayed - learning about triple quotes helped me with this.
		ans = raw_input("Which game would you like to purchase? Please use the corresponding number. ")
# Now I directly ask the user to choose a game.
		if ans == "1":
			print "You are purchasing Zelda."
			m = input("Please provide payment for your selection. ")
			a = m - 10.00
			if a < 0:
				print "Sorry, that is not enough to cover the cost of the game."
				gamemenu()
			if a >= 0:
				print "Your change is " + str (a) + "$" + " thank you for shopping at Old-Mart."
# Depending on the game, the price varies. So I ask for a payment input and then return their balance.
# In each case, if their payment amount is less than the price of the game - they are notified that they do not have enough money.
# If the payment amount is greater, they are returned that value in change.		
		elif ans == "2":
			print "You are purchasing Sonic."
			m = input("Please provide payment for your selection. ")
			a = m - 8.99
			if a < 0:
				print "Sorry, that is not enough to cover the cost of the game."
				gamemenu()
			if a >= 0:
				print "Your change is " + str (a) + "$" + " thank you for shopping at Old-Mart."
		
		elif ans == "3":
			print "You are purchasing Mario."
			m = input("Please provide payment for your selection. ")
			a = m - 15.00
			if a < 0:
				print "Sorry, that is not enough to cover the cost of the game."
				gamemenu()
			if a >= 0:
				print "Your change is " + str (a) + "$" + " thank you for shopping at Old-Mart."
		
		elif ans == "4":
			print "You are purchasing Asteroids."
			m = input("Please provide payment for your selection. ")
			a = m - 2.00
			if a < 0:
				print "Sorry, that is not enough to cover the cost of the game."
				gamemenu()
			if a >= 0:
				print "Your change is " + str (a) + "$" + " thank you for shopping at Old-Mart."
		
		elif ans == "5":
			print "Please come back later!"
			ans = None
# If they choose to exit the menu, this closes the infinite loop and they are taken to the next program.

		else:
			print ("\nNot a valid selection, please try again.")
# This statement catches any input that do not pertain to a menu item.
		
def main():
# This is my main function which allows the user to decide to purchase a game.
	a = raw_input("Ready to buy a game? ").lower().strip()
	if a == "yes":
		gamemenu()
# This if-statement runs the menu function which displays the games and prices to the user.
	else:
		print "Thank you, come again."
# When the user no longer wants to purchase a game, they are thanked and the code moves on.

		
main()
# This calls the main function, which is the first function I want to run.

#################################### Compound Interest Function ###################

print "Compound Interest Calculator.\n"

def compoundinterest(Principal, InterestRate, N, T):
# Here the variables are parsed in and then converted.
	A = Principal * pow(( 1 + (InterestRate/N)),(N*T))
	print "Initial investment = "+str(Principal)+"$, Interest rate = "+str(InterestRate*100.0)+"%, Invested for a total of "+str(T)+" years, compounding "+str(N) + " times per year."
	print "The total value of your investment will be " + str(A) + "$"
# CI is found given the user input, and then a detailed statement is printed showing the value of each variable in another context. Finally, the answer is printed.

def main():
# This is my main function where the user enters the components to be calculated.
	Principal = input("Enter the principal amount of money invested. ")
	InterestRate = input("What is the interest rate? ")
	N = input("How many times per year is the interest compounded? ")
	T = input("How many years will the money be invested? ")
# These are all the variables important to compount interest.
	compoundinterest(Principal, InterestRate, N, T)
# Here is where they are parced to the calculator.
	a = raw_input("Respond 'yes' to continue. ").lower().strip()
	if a == "yes":
		main()
	else:
		print "Thanks!"
# Again, here is a block that allows the user to repeat the functions above.
		
main()
# This calls my input function.

################################## Annuity Function ################################
print "Annuity Value Calculator.\n"

def annuity(PMT, InterestRate, N):
# This function takes in the variables from the main function and then produces the desired calculation then outputs it. 
	P = PMT * (( 1 - pow((1+InterestRate),-N))/InterestRate)
# Here is the conversion formula for the calculation.
	print "The present value of the annuity stream to be paid in the future is " + str(P) + "$"
# This line returns what the user wants to know given the information they entered earlier.
	
def main():
# This is my main function where the user enters the components to be calculated.
	PMT = float(input("What is the amount of each annuity payment? "))
	InterestRate = input("What is the interest rate? ")
	N = input("How many periods are there over which payments are to be made? ")		
# The pertinent variables have been prompted by the code and entered by the user.
	annuity(PMT, InterestRate, N)
# The variables are now parsed to the function that calculates the desired quantity.
	a = raw_input("Respond 'yes' to continue. ").lower().strip()
	if a == "yes":
		main()
	else:
		print "Thanks!"
# This entire section is just here to ask the user if they want to use the code again to do multiple calculations at one time.
		
main()
# This calls the main function, which is the first function I want to run.


