# Reading the input string from the user
input_string = input("Type in a phrase : ")
# Counter used to check if character is odd or even for the first part of task
count = 0
# Variable to hold the string when each character is changed to upper or lower depending on position
upper_lower_input = ""

for char in input_string:
    if(count % 2 == 0):
        upper_lower_input += char.lower()
    else:
        upper_lower_input += char.upper()
    count += 1

print(upper_lower_input)


# Second half of the task

# Creating a list with the words in the original string
split_input = input_string.split() 
 # Resetting the counter to use a mechanism similar to the one used on the 1st half of the task
count = 0

for word in split_input:
    if(count % 2 == 0):
        split_input[count] = word.lower()
    else:
        split_input[count] = word.upper()
    count += 1

# Creating new string with the processed upper and lower case words
new_string = " ".join(split_input)
print(new_string)