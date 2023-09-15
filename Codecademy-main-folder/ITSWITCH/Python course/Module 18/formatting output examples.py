salary = 44000
txt="you make {} pounds a year"
print(txt.format(salary))


string = "Bill learning {}{}."
print(string.format("cyber","security"))

string = "Bill loves {1} {3}, and has {2} {0}."
print(string.format("kids", "cyber", 7,"security"))


string = "Bob likes to play {act} and eat {1}{0}."
print(string.format("dogs", "hot", act="games"))


print("Bob likes to play {act} and eat {1}{0}.".format("dogs","hot", act="games"))
