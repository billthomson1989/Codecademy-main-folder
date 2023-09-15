import random
#Task1
name = "Tuffour"
#Task2
question = "Are you really magic as you are addressed!"
#Task3
answer = ""
#Task5
random_number = random.randint(1, 10)
#print(random_number)

#control flow program(if, elif and else statement)
if random_number == 1:
  answer = "Yes - definitely." 
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Not Sure Sir/Madam."
else:
  answer = "Error"

# optional challenge-13
if name == "":
  print(question)
  print("Magic 8-Ball's answer:" + " " + answer)
else:
  print(name + " " + "asks:" + " " + question)
  print("Magic 8-Ball's answer:" + " " + answer)

# optional challenge-14

# if question == "" and name == "":
  # print("No question and name supplied!!!")
# else:
  # print(name + " " + "asks:" + " " + question)
  # print("Magic 8-Ball's answer:" + " " + answer)

# On default the program is set to a name and a question and it runs as expected but you can manipulate by setting either name or question or even both to an empty string and uncomment the optional challenge-14 for results.