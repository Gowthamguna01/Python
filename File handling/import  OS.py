import os
if os.path.exists("append.txt"):
    os.remove("append.txt") #remove only files

else:
    print("The file doesn't exist")

----------------------------------------------------------


import os
os.rmdir("myfolder")  #remove only folders
