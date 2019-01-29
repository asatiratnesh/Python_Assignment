# Python program to print all natural numbers from 1 to n


def naturalNo(num):
    i = 1
    if num <= 1:
        print "Number should be natural"
    while i <= num:
        print i
        i = i + 1


number = input("Enter no.: ")
naturalNo(number)
