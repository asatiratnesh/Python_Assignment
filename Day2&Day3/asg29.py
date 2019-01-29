# Python program to print Pascal triangle upto n rows.

num = input("Enter no.: ")

for x in range(0, num):
    for y in range(0, x):
        print y
    print "\n"
