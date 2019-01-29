# Python program to print all Prime numbers between 1 to n.

num = input("Enter no.: ")
print [y for y in range(1, num) if all([y % x for x in range(2, y)])]
