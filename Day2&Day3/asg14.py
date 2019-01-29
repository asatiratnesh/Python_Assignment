# Python program to calculate sum of digits of a number.

num = input("Enter no.: ")

total = 0
while num / 10:
    total = total + (num % 10)
    num = num / 10
    if num < 10:
        total = total + (num % 10)
print total
