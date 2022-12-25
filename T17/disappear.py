# Reading the input string from the user
input_string = input("Type in a string : ")
disappearing_chars = input("Type in the characters you want to remove from the previous string with no spaces between them: ")
 # Place holder for modified string
new_string = input_string

for char in disappearing_chars:
    # Using replace to replace the characters to be removed
    new_string = new_string.replace(char, "")

print(new_string)