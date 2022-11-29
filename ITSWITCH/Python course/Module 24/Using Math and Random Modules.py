#Random Module

import random
print("Print a random number")
print(random.random())


print("--------------------------------------")
import random

print("Printing a random integer", random.randint(0, 1000))
print("Printing a random integer", random.randrange(0, 500, 2))

print("--------------------------------------")


#Math has tons of operations and we can't list them all out here like mentioned during the lecture

import math

num = int(input("Please enter a number to find the square root for: "))
print(math.sqrt(num))
