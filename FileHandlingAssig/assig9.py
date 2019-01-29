# find out count of all the python files in any specific directory and subdirectory

import os

# Open a file
path = raw_input("Enter Dir Path: ")
count = 0

for root, dirList, fileList in os.walk(path):
   for x in fileList:
       if x.endswith(".py"):
           count += 1

print "Count of python files in any specific directory and subdirectory: ", count
