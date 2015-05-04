"I am 6'2\" tall." # escape double-quote inside string
'I am 6\'2" tall.' # escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# study drills
print "%r\n%r" % ("MEME", 'meme')
print "\"%r\"" % "Hello"
print "\'%r\'" % "Hello"
print "\"%s\"" % "Hello"
print "\'%s\'" % "Hello"
print "%r" % "\"Hello\""