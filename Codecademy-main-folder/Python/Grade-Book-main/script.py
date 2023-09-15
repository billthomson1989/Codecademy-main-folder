last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

# subjects list
subjects = ["physics","calculus","poetry","history"]
# grades list
grades = [98,97,85,88]

# Creating gradebook list without any method
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history",88]]


#Adding computer science score to the gradebook
gradebook.append(["computer science", 100])
#Adding visual arts score to the gradebook
gradebook.append(["visual arts", 93])
gradebook[5][1] = 98

# changing the value of poetry grade to boolean
gradebook[2].remove(85)
gradebook[2].append("Pass")

full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)