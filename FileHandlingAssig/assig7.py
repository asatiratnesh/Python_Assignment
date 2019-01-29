# read csv file which contain following columns emp id, emp name, empsal, empdept

fileHandle = open("empData.csv", "r")

columns = list()
all_data = dict()
listKeys = fileHandle.readline().split(",")

# for row in fileHandle.readlines():
#     column_values = row.split(',')
#     all_data.append({key: value for key, value in zip(listKeys, column_values)})
for column in listKeys:
    all_data[column] = list()

for row in fileHandle.readlines():
    row_list = row.split(',')
    i = 0
    for column in listKeys:
        all_data[column].append(row_list[i])
        i += 1

count = 0
sum = 0

for x in all_data['emp_dept\n']:
    if x == "IT\n":
        sum = sum + int(all_data['emp_salary'][count])
        count += 1
    else:
        count += 1

print sum/len(all_data['emp_salary'])
