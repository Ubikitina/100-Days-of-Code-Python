# === Reading a File ===

# Open the file named "my_file.txt" for reading (by default) and create a file object
file = open("my_file.txt")

# Read the contents of the file and store them in the variable "contents"
contents = file.read()

# Print the contents of the file to the console
print(contents)

# Close the file to release system resources
file.close()

# Same functionality as before but this time, we use with statement to automatically close the file when the block of code is exited, ensuring a better resource management
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)



# === Writing a File ===
with open("my_file.txt", mode="w") as file: # "w" mode replaces the text with new one
    file.write("New text.")

with open("my_file.txt", mode="a") as file: # "a" mode appends the new text at the end
    file.write("New text.")