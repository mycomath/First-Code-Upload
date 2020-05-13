print "Welcome to the compound interest calculator. You can easily determine how your investment will grow."

Principal = input("Enter the principal amount of money invested. ")
InterestRate = input("What is the interest rate? ")
N = input("How many times per year is the interest compounded? ")
T = input("How many years will the money be invested? ")

A = Principal * pow(( 1 + (InterestRate/N)),(N*T))

print "With an initial investment of "+str(Principal)+"$, at an interest rate of "+str(InterestRate*100.0)+"%, invested for a total of "+str(T)+" years, compounding "+str(N) + " times per year."
print "The total value of your investment will be " + str(A) + "$"