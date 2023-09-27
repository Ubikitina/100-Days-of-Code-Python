# Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

with open("./Input/Names/invited_names.txt") as file:
    invited_names = [line.strip() for line in file]

#for each name in invited_names.txt
for name in invited_names:
    #Replace the [name] placeholder with the actual name.
    finished_letter = starting_letter.replace("[name]", name)
    #Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(finished_letter)

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp