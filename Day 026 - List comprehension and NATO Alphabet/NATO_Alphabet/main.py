import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# with open("nato_phonetic_alphabet.csv", mode="r") as file:
    # csv_reader = csv.reader(file)
    # nato_alphabet_list = [row for row in csv_reader if row[0] != "letter"] # new_list = [new_item for item in list]

# There's no need to open and close the file n pandas, read_csv method  does for us
nano_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# print(nano_alphabet_df)

# Create a dictionary in this format:
nano_alphabet_dict = {row.letter:row.code for (index, row) in nano_alphabet_df.iterrows()}
# print(nano_alphabet_dict)

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please enter a word: ").upper()
word_list = [nano_alphabet_dict[letter] for letter in user_input if letter in nano_alphabet_dict]
print(word_list)
