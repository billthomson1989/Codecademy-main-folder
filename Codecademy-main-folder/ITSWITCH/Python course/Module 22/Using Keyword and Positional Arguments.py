#Using Keyword and Positional Arguments

def greet(name,msg=" How are you today?"):
    print("Hey",name + "," + msg)

print("2 keyword arguments")
greet(name = "Bill", msg = " How do you do?")
print("-----------------------------------------")

print("2 keyword aguments (out of order)")
greet(msg = " How are you doing?", name = "Bill")
print("-----------------------------------------")

print("1 positional, 1 keyword argument")
greet("Bill", msg = " How do you doin?")
print("-----------------------------------------")

greet("Bill") #isn't needed and doesn't change because our default value at the beginning automatically using the name and msg
