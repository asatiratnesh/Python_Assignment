# find out total no of lines total no of words total no of characters in file

fileHandle = open("abc.txt", "r")

noLines = len(fileHandle.readlines())
noWords = 0
noCharacters = 0
print "No. of Lines: ", noLines

fileHandle.seek(0)

for i in range(0, noLines):
    noWords += len((fileHandle.readline()).split())

print "No. of Words: ", noWords

fileHandle.seek(0)
print "No. of characters: ", len((fileHandle.read()).strip())
