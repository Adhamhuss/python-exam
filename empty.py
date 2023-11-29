
#asking the user to input between 1 or 2
option = input("pick option: 1 for english to morse code, 2 for morse code to english\n")


#morse code dictionary
morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

# define the function to translate from english to morse code
def english_to_morse_code(text):
    morse_code_text = ''
    for char in text:
        if char.upper() in morse_code:
            morse_code_text += morse_code[char.upper()] + ' '
        else:
            morse_code_text += char
    return morse_code_text

# define the function to translate from morse code to  english
def morse_code_to_english(text):
    english_text = ''
    morse_code_list = text.split(' ')
    for code in morse_code_list:
        for char, morse in morse_code.items():
            if code == morse:
                english_text += char
        if code == '':
            english_text += ' '
    return english_text


# here it checks what the use has inputted and translates accordingly
if option == '1':
    english_text = input("Enter the english text you would like to translate to morse:\n")
    morse_code_text = english_to_morse_code(english_text)
    print("Morse Code: ", morse_code_text)
elif option == '2':
    morse_code_text = input("enter the morse code to translate to english:\n")
    english_text = morse_code_to_english(morse_code_text)
    print("English: ", english_text)
else:
    print("The option you have picked is invalid. please pick 1 or 2")