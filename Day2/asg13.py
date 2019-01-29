# Python program to swap first and last digits of a number.

num = input("Enter no.: ")

i = 1
numnew = 0
while num / 10:
    num = num / 10
    i += 1

while 0 < i:
    num = num / 10
    numnew = num * 10
    i -= 1

print numnew
