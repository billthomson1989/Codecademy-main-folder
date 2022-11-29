with open("Hello.txt","w")as file:
    file.write("Hey there!")

x=open("Hello.txt","r")
print(x.read())
x.close()
