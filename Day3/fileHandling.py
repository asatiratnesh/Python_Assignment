
fileABC = open("abc.txt", 'r')

# close()
# closed
# read()
# readline()
# readlines()
# seek()
# tell()
# write()
# writelines()

# help(fileABC.seek)

print fileABC.read(4)
print fileABC.tell()

allfiles = list()

for i in range(1000):
    with open("file1.txt", 'w') as infile:
        infile.write("Tis is line 1\n")
        allfiles.append(infile)
