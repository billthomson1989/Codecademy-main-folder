import shutil
import os

x=open("Createme1.txt","x")
x.close()

x=open("Createme1.txt","a")
x.write("I hope this example appears"'\n')
x.write("If all goes well it will appear"'\n')
x.close()

src = "Createme1.txt"
dst = "Createme2.txt"

shutil.copy(src, dst)


a = open("Createme2.txt", "a")
a.write("\nHere is another line in our text file ")
a.close ()

x=open("Createme2.txt","r")
print(x.read())


#Second method using while loops

x=open("Createme2.txt","a")
b=1
while b <4:
    x.write("Time for a new line" +str(b)+"\n")
    b+=1
x.close()

first=open("Createme1.txt","r")
print(first.read())
first.close()

second=open("Createme2.txt","r")
print(second.read())
second.close()
