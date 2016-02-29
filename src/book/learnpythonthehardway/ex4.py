# Exercise 4 - Variables and Names

cars = 100

space_in_a_car = 4.0

drivers = 30

passengers = 90

cars_not_driven = cars - drivers

cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car

average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available"

print "There are only", drivers, "drivers available"

print "There will be", cars_not_driven, "empty cars today"

print "We can transport", carpool_capacity, "people today"
print "We have", carpool_capacity, "to carpool today"

print "We need to put about", average_passengers_per_car, "passengers in each car"

# ex 5

# Output Formatting

# Using  formatting characters - Old way

print "If I add %d and %d, I get %d" % (1, 2, 1 + 2)

name = "Python!"
print "Hello, %s" % name

# More on formatting - https://docs.python.org/2.4/lib/typesseq-strings.html


# New Style

print "If I add {} and {}, I get {}".format(1, 2, 1 + 2)

import math

print "The value of Pi is approximately {0: .3f}".format(math.pi)

# Passing an integer after the ':' will cause that field to be a minimum number of characters wide.
# This is useful for making printing tables pretty.

table = {'Jack': 4127, 'John': 4098, 'Debby': 7678}

for name, phone in table.items():
    print "{0:10} ==> {1:10d}".format(name, phone)
