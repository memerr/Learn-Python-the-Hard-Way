# creates a variable x and sets it value to string with a format string d, which means a signed integer decimal
x = "There are %d types of people." % 10
# creates a variable binary and sets a string value of binary
binary = "binary"
# creates a variable do_not and sets a string variable of don't
do_not = "don't"
# creates a variable y and sets a string value with a format string s, which converts an object to a string
y = "Those who know %s and those who %s." % (binary, do_not)

# prints the value of the variable x
print x
# prints the value of the variable y 
print y

# prints a string value with a format string r, which puts the value in a string like "'text'"
print "I said: %r." % x
# prints a string value with a format string s, which converts an object to a string
print "I also said: '%s'." % y

# creates a variable with a boolean value of False
hilarious = True
# creates a variable with a string value plus a format string that doesn't have a value yet
joke_evaluation = "Isn't that joke so funny!? %r"

# prints the value of the variable joke_evaluation, but now with a value for the format string r
print joke_evaluation % hilarious

# creates a variable with a string value
w = "This is the left side of..."
# creates a variable with a string value
e = "a string with a right side."

# concatenates the string values of w and e
print w + e