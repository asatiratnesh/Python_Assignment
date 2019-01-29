# convert each n every word in upper case in file

fileHandle = open("abc.txt", "r")
fileHandle.seek(0)
upperString = (fileHandle.read()).upper()
fileHandle.close()

fileHandleWrite = open("abc.txt", "w")

fileHandleWrite.write(upperString)
fileHandleWrite.close()
