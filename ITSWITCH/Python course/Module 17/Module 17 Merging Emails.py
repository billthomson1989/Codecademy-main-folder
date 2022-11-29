with open("Names.txt",'r') as namefile:
    with open("Message.txt",'r') as messagefile:
        body= messagefile.read()
        for name in namefile:
            mail = "Hello " + name + body
            with open(name.strip()+".txt",'w') as messagefile:
                messagefile.write(mail)

print("All done, Messages created and ready, take a look in your folder")
print("----------------------------------------------------------------")
print("Here is an example of the messages created\n")

with open("Billy.txt", "r") as bills:
    print(bills.read())
