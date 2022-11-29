#Trapping for numbers
txt = input("Give me a number:")


try:
    num = int(txt)
    print("You entered the number",num)
except ValueError:
    print("Please put in a number in numeral format, not in alphabet format.")
