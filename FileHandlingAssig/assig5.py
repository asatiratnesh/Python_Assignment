# count of each and every word in file

fileHandle = open("abc.txt", "r")
print len((fileHandle.read()).split())
