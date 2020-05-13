# 
# Author       : Andrew Caudill
# Date         : 2018.02.08
# Version      : 0.0.1
# Email        : acaudill5@radford.edu
# Assignment   : Homework 01
# Description  : Source code for Homework 01. Currency converter.
# 
#############################################

print "Thank you for choosing Currency Converter."
startingcurrency = input ("Please specify the type of currency you currently own (USD=1, EURO=2, YEN=3).")
endingcurrency = input ("Please specify the type of currency you wish to convert to (USD=1, EURO=2, YEN=3).")
m = float(input("Please enter the amount of currency you wish exchange here."))
# These input prompts give the user the ability to select the currency they need and then convert it.

if startingcurrency==1 and endingcurrency==2:
	print "I see that you are converting from USD to EURO."
	a = m * 0.8817
	b = "EURO"
elif startingcurrency==1 and endingcurrency==3:
	print "I see that you are converting from USD to YEN"
	a = m * 109.556
	b = "YEN"
elif startingcurrency==2 and endingcurrency==1:
	print "I see that you are converting from EURO to USD"
	a = m / 0.8817
	b = "USD"
elif startingcurrency==3 and endingcurrency==1:
	print "I see that you are converting from YEN to USD"
	a = m / 109.556
	b = "USD"
# Each if statement corresponds to a possible currency conversion, each with a unique conversion rate. 
# They also determine the end currency type and the value of the converted currency.
else:
	print "\nThat conversion is not accepted, please try again.\n"
# This statement covers inputs that aren't expected.

print "Before conversion fees, your foreign currency amounts to" + ' ' + str(a) + " " + str(b) + "."
# print "text" + str(a)
# This gives a user the gross amount of currency converted, before fees are assessed.
	
companyAfee = a * 0.15
companyAtotal = a * 0.85
# Here are the fee and total rates for Company A.

print "Your fee for Company A is " + str(companyAfee) + str(b) + " therefore, your total comes to " + str(companyAtotal) + str(b) + "."
# This statement prints both the fee and the converted amount through Company A.
if endingcurrency == 1:
	x = 30
	
elif endingcurrency == 2:
	x = 30 * 0.8817
	
elif endingcurrency == 3:
	x = 30 * 109.556
# These statements are exclusively for Company B. Since they charge a flat rate in USD, I assess the same amount in each
# currency depending on which currency they end with.
companyBtotal = a - x
# Since the rate is flat, the total is the gross - fee.

print "Your fee for Company B is " + str(x) + str(b) + ";therefore, your total comes to" + str(companyBtotal) + str(b) + "."
# This statement prints both the fee and converted total from Company B.

if companyAtotal > companyBtotal:
	print "Company A provides a better exchange rate."
	
elif companyBtotal > companyAtotal:
	print "Company B provides a better exchange rate."
	
elif companyAtotal == companyBtotal:
	print "Both companies provide the same exchange rate."
#These statements are for the user. They show which Company provides the best exchange rate given the total converted amount.

print "Thank you for using Currency Converter."

	
	
	


