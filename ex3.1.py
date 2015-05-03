# code for caclulating the perimeter of a rectangle
print "Calculate the perimeter of a rectangle"

# ask for width
width = raw_input("Please enter the width in centimeters: ")
# ask for length
length = raw_input("Please enter the length in centimeters: ")

perimeter = 2 * float(width) + 2 * float(length)
print "The perimeter of the rectangle is:", perimeter, "cm"