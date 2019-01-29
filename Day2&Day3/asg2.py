# Python program to print all natural numbers in reverse (from n to 1)


def naturalNo(num):
    i = num
    if num < 0:
        print "Number should be natural"
    while 1 <= i:
        print i
        i = i - 1


number = input("Enter no.: ")
naturalNo(number)
