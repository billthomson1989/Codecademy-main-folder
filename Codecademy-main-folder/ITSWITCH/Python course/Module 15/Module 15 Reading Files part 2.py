print("------------------------------------------")

with open("demo.txt.") as myfile:
    contents = myfile.read()
    print(contents)

a = open("demo.txt", "a")
a.write("\nHere is another line in our text file")
a.close ()

print("------------------------------------------")

with open("demo.txt.") as myfile:
    contents = myfile.read()
    print(contents)


    
