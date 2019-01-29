# Python program to calculate product of digits of a number.

num = input("Enter no.: ")

product = 1
while num / 10:
    product = product * (num % 10)
    num = num / 10
    if num < 10:
        product = product * (num % 10)
print product
