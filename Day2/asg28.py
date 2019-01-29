# Python program to print Fibonacci series up to n terms.

num = input("Enter no.: ")
num2 = 0
num3 = 1
for i in range(1, num+1):
    next = num2 + num3
    num2 = num3
    num3 = next
    print next