# accept a file name and directory name from user and create a backup of this file in same directory

fileName = raw_input("Enter file name: ")
directoryName = raw_input("Enter directory name: ")

f = open(directoryName+fileName+".txt", "w")
