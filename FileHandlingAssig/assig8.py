# accept directory name from user and remove if it is modify 30days older and if size is 100kb

import time, datetime
import os

# Open a file
path = "fileDir"
dirs = os.listdir(path)

modifyTime = time
print modifyTime
# This would print all the files and directories
for file in dirs:
    if modifyTime < time.ctime(os.path.getmtime(file)):
        modifyTime = time.ctime(os.path.getmtime(file))
print modifyTime
