# declare no. of car variable and assign value
cars = 100
# declare passenger space in car variable and assign value
space_in_a_car = 4.0
# declare no. of drivers variable and assign value
drivers = 30
# declare total no. of passengers variable and assign value
passengers = 90
# calculate total cars not driven to driver
cars_not_driven = cars - drivers
# calculate total cars driven
cars_driven = drivers
# calculate carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# calculate average of passengers in each car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
