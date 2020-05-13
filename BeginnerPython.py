print "Hello world!"
# Prints the string contained in the quotes.

msg = "Hello world!"
print (msg)
# Prints the string data associated with the variable.

first_name = "albert".title()
last_name = "einstein".title()
full_name = first_name + " " + last_name
print (full_name)
# Allows concatenation of data types by aligning them. In this case we are combining strings.

bikes = ['trek', 'mountain', 'racing', 'dirtbike']
# This is how to make a list.

first_bike = bikes[0]
# Returns the first item in the list.

last_bike = bikes[-1]
# Returns the last item in the list.

for bike in bikes:
	print(bike)
# Loops through the list.

bikes = []
bikes.append ("motor")
bikes.append ("trike")
bikes.append ("big wheel")
# Allows adding items to a list.

squares = []
for x in range(1, 11):
	squares.append(x**2)
	print squares
# Making numerical lists.

squares = [x**2 for x in range(1, 11)]
# List comprehensions ???

finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[ :2]
print finishers
# This allows slicing of a list.

copy_of_bikes = bikes[:]
# Copies a list.

Tuple =(1920, 1080)
print Tuple

def greet_user(username):
	"""Display a personalized greeting."""
	print("Hello, " + username +"!"
	
greet_user.("jesse")