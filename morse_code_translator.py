import re


user_input = input("Enter the morse code: ")
def get_translation(user_input):
    translation = ""
    if user_input.isalpha():
        morse_code = user_input
        for element in morse_code:
            # try:
            translation += val_list[key_list.index(element)]    
            # except ValueError:
            #     return False
    else:
        morse_code = user_input.split()
        for element in morse_code:
            # try:
            translation += key_list[val_list.index(element)]
            # except ValueError:
            #     return False
    return translation
    


morse_code_dict = {
    ".-":"a",
    "-...":"b",
    "-.-.":"c",
    "-..":"d",
    ".":"e",
    "..-.":"f",
    "--.":"g",
    "....":"h",
    "..":"i",
    ".---":"j",
    "-.-":"k",
    ".-..":"l",
    "--":"m",
    "-.":"n",
    "---":"o",
    ".--.":"p",
    "--.-":"q",
    ".-.":"r",
    "...":"s",
    "-":"t",
    "..-":"u",
    "...-":"v",
    ".--":"w",
    "-..-":"x",
    "-.--":"y",
    "--..":"z", 
    ".----":"1",
    "..---":"2",
    "...--":"3",
    "....-":"4",
    ".....":"5",
    "-....":"6",
    "--...":"7",
    "---..":"8",
    "----.":"9",
    "-----":"0",
    ".-.-.-":".",
    "..--..":",",
    "--..--":"!",
    "........":" "
}
key_list = [morse_code_dict.keys()]
val_list = [morse_code_dict.values()]

print(get_translation(user_input))