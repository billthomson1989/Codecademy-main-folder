#Writing Files
print("------------------------------------------------")

a=open("BillFile.txt","w")
a.write("There should be some text here now")
a.close()


print("------------------------------------------------")
print("Module 15 practice")

with open("BillFile.txt.") as myfile:
    contents = myfile.read()
    print(contents)

x="Testing my While Loop. Writing something. Because I need 3 lines."
y=1
while y<=3:
    print(x)
    y+=1

