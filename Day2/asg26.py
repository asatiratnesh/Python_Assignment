# Python program to check whether a number is Armstrong number or not.

num = input("Enter no.: ")

list1 = [int(x)**len(str(num)) for x in str(num)]
if num == sum(list1[0:len(list1)]):
    print "Is Armstrong"
else:
    print "Is not Armstrong"
