def alpha_to_morse_tranlation(code):
    """translates normal text to morse code"""
    if type(code) != str:
        raise ValueError
    else:
        translation = ""
        for element in code:
            try:
                translation += morse_sings_l[letters_l.index(element)] + " "    
            except ValueError:
                return False
        return translation
   

def morse_to_alpha_translation(code):
    """translates morse code to normal text"""
    translation = ""
    morse_code = code.split()
    for element in morse_code:
            try:
                translation += letters_l[morse_sings_l.index(element)]
            except ValueError:
                return False
    return translation
    

letters_l =[
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z", 
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    ".",
    ",",
    "!",
    " "
]

morse_sings_l = [".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",
    ".----",
    "..---",
    "...--",
    "....-",
    ".....",
    "-....",
    "--...",
    "---..",
    "----.",
    "-----",
    ".-.-.-",
    "..--..",
    "--..--",
    "........"
]
translator_choice = input("Which way do you want to translate? 1 for morse to text; 2 for text to morse: ").strip().lower()
code = input("Enter the morse code: ")
if translator_choice == "1":
    print(morse_to_alpha_translation(code))
elif translator_choice == "2":
    print(alpha_to_morse_tranlation(code))
else:
    print("invalid input, enter 1 or 2 to chose between translators")