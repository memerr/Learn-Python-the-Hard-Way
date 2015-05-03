print "I will now count my chickens:"

# (30 divided by 6 = 5) plus 25 = 30
print "Hens", 25 + 30 / 6
# (25 times 3 = 75) (75 modulo 4 = 3) or (75 divided by 4 = 18 remainder 3) -> 100 minus 3 = 97
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

# (4 module 2 = 0) (1 divided by 4 = 0) 3 + 2 + 1 - 5 + 0 - 0 + 6 = 7
# changed 1 to 1.0 (1 - .25 + 6) left to right
print 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

# (3 add 2 = 5) < (5 less 7 = -2) -> 5 is not less than -2
print 3 + 2 < 5 - 7

# 3 add 2 = 5
print "What is 3 + 2?", 3 + 2
# 5 less 7 = -2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

# checks if 5 is greater than negative 2
print "Is it greater?", 5 > -2
# checks if 5 is greater than or equal to negative 2
print "Is it greater or equal?", 5 >= -2
# checks if 5 is less than or equal to negative 2
print "Is it less or equal?", 5 <= -2