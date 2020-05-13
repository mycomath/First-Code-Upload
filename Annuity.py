print "Welcome to the Annuity Value Assesser."

PMT = input("What is the amount of each annuity payment? ")
InterestRate = input("What is the interest rate? ")
N = input("How many periods are there over which payments are to be made? ")

P = PMT * (( 1 - pow((1+InterestRate),-N))/InterestRate)

print "The present value of the annuity stream to be paid in the future is " + str(P) + "$"