# Python program to calculate factorial of a number.

num = int(input("Enter no.:"))
fact = lambda num:1 if num==0 else num*fact(num-1)
print fact(num)
