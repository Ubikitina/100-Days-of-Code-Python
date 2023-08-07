#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

random_number = random.randrange(0,2)

if random_number == 1:
    print("Heads")
elif random_number == 0:
    print("Tails")
else:
    print("Invalid output")