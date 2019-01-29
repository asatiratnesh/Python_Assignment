# Python program to find frequency of each digit in a given integer.

num = str(input("Enter no.: "))

nocount = [num.count(el) for el in num]
nocount = list(nocount)
dict = {num[i]: nocount[i] for i in range(len(nocount))}
print dict