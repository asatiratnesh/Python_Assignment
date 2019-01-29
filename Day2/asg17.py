# Python program to check whether a number is palindrome or not.

num = input("Enter no.: ")
num2 = str(num)[::-1]
if int(num2) == num:
    print True
else:
    print False
