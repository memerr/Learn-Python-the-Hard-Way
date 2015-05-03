# creates a variable called cars and sets a value of 100 to it
cars = 100
# creates a variable called space_in_a_car and sets a value of 4.0 to it
space_in_a_car = 4.0
# creates a variable called drivers and sets a value of 30 to it
drivers = 30
# creates a variable called passengers and sets a value of 90 to it
passengers = 90
# creates a variable called cars_not_driven and sets a value of (the values of the variable cars minus the value of the vraible drivers)
cars_not_driven = cars - drivers
# creates a variable called cars_driven and sets its value to the value of the variable drivers
cars_driven = drivers
# creates a variable called carpool_capacity and sets its value to the value of cars_driver multiplied by the value of space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# creates a variable called average_passengers_per_car and sets a value of (the value of passengers divided by the value of cars_driven)
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available"
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."