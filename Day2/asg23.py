# Python program to find LCM of two numbers.

num = int(input("Enter first no.:"))
num2 = int(input("Enter second no.:"))

hcf = 0
numlist = []
numlist2 = []

for x in range(2, num+1):
    if not num % x:
        numlist.append(x)
        num = num / x
        if num < x:
            numlist.append(num)

for x in range(2, num2+1):
    if not num2 % x:
        numlist2.append(x)
        num2 = num2 / x
        if num2 < x:
            numlist2.append(num2)
lcm = 1


def multiplyList(list1):
    result = 1
    for x in list1:
        result = result * x
    return result

for i in numlist:
    if i in numlist2:
        lcm = lcm * i
        numlist2.remove(i)
    else:
        lcm = lcm * i

lcm = lcm * multiplyList(numlist2)

print lcm
