# Python program to count number of digits in a number.

# print len(str(input('Enter No.: ')))

num = input("Enter no.: ")

i = 1
while num / 10:
    num = num / 10
    i += 1
    if num < 10:
        break
print i
