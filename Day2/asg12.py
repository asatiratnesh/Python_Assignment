# Python program to find sum of first and last digit of a number.

num = input("Enter no.: ")

i = 0
first = 0
last = 0
while num / 10:
    if i == 0:
        last = num % 10
    num = num / 10
    if num < 10:
        first = num % 10
    i += 1

print first + last
