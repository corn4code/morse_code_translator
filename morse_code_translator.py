from re import S


user_input = input("Enter the morse code: ")
translation = ""
morse_code = user_input.split()
for element in morse_code:
    if element == "...":
        letter = "s"
        translation += letter

    if element == "---":
        letter = "o"
        translation += letter


print(translation)