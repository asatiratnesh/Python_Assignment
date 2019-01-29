# Python program to find HCF (GCD) of two numbers.

num = int(input("Enter first no.:"))
num2 = int(input("Enter second no.:"))

hcf = 0
if num > num2:
    ls = [x if not (num % x) else 0 for x in range(2, num/2)]
    for i in ls:
        if not i == 0:
            if not num2 % i:
                hcf = i
else:
    ls = [x if not (num2 % x) else 0 for x in range(2, num2 / 2)]
    for i in ls:
        if not i == 0:
            if not num % i:
                hcf = i
print hcf

