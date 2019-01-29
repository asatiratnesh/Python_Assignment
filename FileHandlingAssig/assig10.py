# accept directory name from user and remove all the empty files, from that directory.

import os

# Open a file
path = raw_input("Enter Dir Path: ")
dirs = os.listdir(path)

for x in dirs:
    if not os.path.getsize(path+"\\"+x):
        os.remove(path+"\\"+x)
