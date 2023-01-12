# Creating variable to hold string and empty dictionary
sample_string = "Study hard and all things can be accomplished. Give up, and you will amount to nothing."
occurrences_dictionary = {}

# Looping through characters in string and checking if they exist in the dictionary
for character in sample_string:
    if character.lower() in occurrences_dictionary.keys():
        occurrences_dictionary[character.lower()] += 1
    else:
        occurrences_dictionary[character.lower()] = 1

print(occurrences_dictionary)
