print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)

# study drills

print "What's your name?",
name = raw_input()
print "Hello " + name

# math
print "Give the measurement of a side of a square in centimeters:",
x = int(raw_input()) ** 2
print "The square has an area of \'%s\' centimeters" % x