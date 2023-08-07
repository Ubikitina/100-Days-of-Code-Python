# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# The code below calculates the count of occurrences of 'TRUE' letters in both names.
true_letters = "TRUE"
count1_true = sum(name1.upper().count(letter) for letter in true_letters)
count2_true = sum(name2.upper().count(letter) for letter in true_letters)
count_true = count1_true+count2_true

# The code below calculates the count of occurrences of 'LOVE' letters in both names.
love_letters = "LOVE"
count1_love = sum(name1.upper().count(letter) for letter in love_letters)
count2_love = sum(name2.upper().count(letter) for letter in love_letters)
count_love = count1_love+count2_love

# Concatenate the count of TRUE and LOVE occurrences as strings and convert it to an integer to get the love score.
love_score = int(str(count_true)+str(count_love))

# Check the Love Score and print the appropriate message
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")