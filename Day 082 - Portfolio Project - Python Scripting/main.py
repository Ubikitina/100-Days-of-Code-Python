morse_code = {'A': '.-',
              'B': '-...',
              'C': '-.-.',
              'D': '-..',
              'E': '.',
              'F': '..-.',
              'G': '--.',
              'H': '....',
              'I': '..',
              'J': '.---',
              'K': '-.-',
              'L': '.-..',
              'M': '--',
              'N': '-.',
              'O': '---',
              'P': '.--.',
              'Q': '--.-',
              'R': '.-.',
              'S': '...',
              'T': '-',
              'U': '..-',
              'V': '...-',
              'W': '.--',
              'X': '-..-',
              'Y': '-.--',
              'Z': '--..',
              '0': '-----',
              '1': '.----',
              '2': '..---',
              '3': '...--',
              '4': '....-',
              '5': '.....',
              '6': '-....',
              '7': '--...',
              '8': '---..',
              '9': '----.'}

def letter_to_morse(letter):
    return morse_code.get(letter.upper(), 'Unknown') # 'Unknown is the default value in case the specified key (uppercase letter) is not found in the dictionary


# Ask the user for a sentence
user_input = input("Enter a sentence: ")
morse_result = ''

# Call the function and print the result
for char in user_input:
        if char.isalpha() or char.isdigit():
            morse_result += letter_to_morse(char) + ' '
        elif char.isspace():
            morse_result += ' '
        else:
            morse_result = "Error, the string contains unaccepted characters (characters that are neither digits nor letters)."
            break

print(f"Morse code for {user_input}: {morse_result}")