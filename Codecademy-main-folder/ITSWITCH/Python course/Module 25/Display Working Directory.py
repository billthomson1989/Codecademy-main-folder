#Working directory
print("\n")
import os

dirpath = os.getcwd()
print("Your current working directory is:" + dirpath)

foldername = os.path.basename(dirpath)
print("The directory name is:" + foldername)
