# task 1
import csv
# task 12
import json
# task 2
compromised_users = []
# task 3
with open('passwords.csv') as password_file:
  # task 4
  password_csv = csv.DictReader(password_file)
  # task 5
  for password_row in password_csv:
    # task 6
    # print(password_row['Username'])

    # task 7
    compromised_users.append(password_row['Username'])

# task 8
with open('compromised_users.txt', 'w') as compromised_user_file:
  # task 9
  for compromised_user in compromised_users:
    # task 10
    compromised_user_file.write(compromised_user)

# task 13
with open('boss_message.json', 'w') as boss_message:
  # task 14
  boss_message_dict = {
      "recipient": "The Boss",
      "message": "Mission Success"
  }
  # task 15
  json.dump(boss_message_dict, boss_message)
# task 16
with open('new_passwords.csv', 'w') as new_passwords_obj:
  # task 17
  slash_null_sig = """ 
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/ """

# task 18
  new_passwords_obj.write(slash_null_sig)
