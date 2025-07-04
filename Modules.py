# os Module – Interact with System/Files

import os

#Current Working directory
print("Current Working Directory: ", os.getcwd(),"\n")

#List Files in current Dir
print("Files:", os.listdir(),"\n")

#create a new folder
os.mkdir("logs2")

#create a file inside that folder
with open("logs2/status.txt", "w") as f:
    f.write("Server is up\n")

#Check if path exists
print("Does logs2/status.txt exist?", os.path.exists("logs2/status.txt"))


