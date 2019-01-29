# math

import os
import zipfile

dirName = raw_input("Enter Dir Name: ")

if os.path.exists(dirName):
    if os.path.isdir(dirName):
        os.chdir(dirName)
        for root, dirList, fileList in os.walk(os.getcwd()):
            for x in fileList:
                if not os.path.getsize(root+"\\"+x):
                    os.remove(root+"\\"+x)
    print "Empty files removed..."
else:
    print "Not Exists"
