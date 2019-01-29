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

print all_data
