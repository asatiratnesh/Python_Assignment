# Python program to check whether a number is Prime number or not.

num = input("Enter no.: ")
print all([num % x for x in range(2, num)])
