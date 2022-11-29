import shutil
import os

src = "example.txt"
dst = "example2.txt"

shutil.copy(src, dst)

os.rename("example2.txt","I'vebeenrenamed.txt")

x=open("I'vebeenrenamed.txt","r")
print(x.read())
x.close


