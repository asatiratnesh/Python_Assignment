# Python program to print all Armstrong numbers between 1 to n.

num = input("Enter no.: ")

print [a for a in range(1, num+1) if a == sum([int(x)**len(str(a)) for x in str(a)][0:len([int(x)**len(str(a)) for x in str(a)])])]

