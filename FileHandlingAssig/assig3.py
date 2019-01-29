# convert the content of files in reverse order.

fileHandle = open("abc.txt", "r")
fileHandle.seek(0)
revString = fileHandle.read()[::-1]


fileHandleWrite = open("abc.txt", "w")

fileHandleWrite.write(revString)
fileHandleWrite.close()
