from art import logo

# Function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar(text, shift, cipher_direction):
    # Shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text. 
    new_text =""
    if cipher_direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            new_position = alphabet.index(letter)+shift
            if new_position >= len(alphabet):
                new_position = new_position - len(alphabet)
            new_text = new_text + alphabet[new_position]
        else:
            new_text = new_text + letter
    print("Here's the {} result: {}".format(cipher_direction, new_text))

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

restart = True
while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # What if the user enters a shift that is greater than the number of letters in the alphabet?
    shift = shift % len(alphabet)

    if direction == "encode" or direction == "decode":
        caesar(text, shift, direction)
    else:
        print("Enter a valid input.")
    
    user_restart = input("Do you want to restart? Select 'yes' or 'no':\n").lower()
    if not user_restart == "yes":
        restart = False
        print("Goodbye!")
