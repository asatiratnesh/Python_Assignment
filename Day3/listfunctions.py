
l = ["a", "w", "s"]
# help(list.sort)

# l.append("f")
# print l.count("a")
# l.extend(["a", "w", 1])
# print l.index('s', 1)
# l.sort()
# print l

names = ['aakash', 'ajay', 'Amit', 'Ankit']
names.sort(key=str.lower, reverse=False)
print names

nan = sorted(names)  # return new sorted list not modify main list

employee = [['jatin', 30000, 'IT', 'Pune', 30], ['Aaksh', 20000, 'IT', 'Pune', 20], ['Vijay', 40000, 'HR', 'Pune', 24]]

l = sorted(employee, key=lambda x: x[1] if x[2] == "IT" else max([i[1] for i in employee if i[2] == "IT"]) + 1)[:2]
