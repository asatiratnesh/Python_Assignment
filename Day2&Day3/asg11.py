# Python program to find first and last digit of a number.

num = input("Enter no.: ")

i = 0
while num / 10:
    if i == 0:
        print "Last Digit: ", num % 10
    num = num / 10
    if num < 10:
        print "First Digit: ", num % 10
    i += 1

