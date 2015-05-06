# from the module called sys, import argv
from sys import argv

# argv[0] = script, argv[1] = filename
script, filename = argv

# creates a file object of the file and puts it inside the variable txt
txt = open(filename)

print "Here's your file %r:" % filename
# prints a string containing all the characters in the file inside the variable txt
print txt.read()

print "Type the filename:"
# gets input from the user and stores it in the variable file_again
file_again = raw_input("> ")

# creates a file object and stores it in a variable
txt_again = open(file_again)

# prints a string containing all the characters in the file object
print txt_again.read()

txt.close()
txt_again.close()
