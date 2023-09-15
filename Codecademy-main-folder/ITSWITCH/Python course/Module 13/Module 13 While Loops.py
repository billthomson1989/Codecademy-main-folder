#Working with While Loops
print("While Loops")
print("--------------------------------------------")


a=1
while a<6:
    print(a)
    a+=1
print("End of the loop")


print("--------------------------------------------")

x="Hello World"
y=1
while y<=3:
    print(x)
    y+=1
print("End of the 2nd loop")


print("--------------------------------------------")
print("While Loop with Continue")
x=0
while x<6:
    x+=1
    if x != 4:
        continue
    print(x)

print("--------------------------------------------")

x=0
while x<6:
    x+=1
    if x == 4:
        continue
    print(x)


print("--------------------------------------------")
print("While Loop with break")

a=1
while a<14:
    print(a)
    if a==4:
        print("It's equal to 4, time to stop")
        break
    a += 1


print("-------------------------------------------------")
print("Module 13 practice")

x="Great Job"
y=1
while y<=3:
    print(x)
    y+=1


print("-------------------------------------------------")


a=1
while a<10:
    print(a)
    if a==6:
        print("It's equal to 6, time to stop")
        break
    a += 1
