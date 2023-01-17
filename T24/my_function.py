# Defining a function that prints all days of the week
def days_of_week():
    days = ("\nMonday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\nSunday")
    return days


# Defining a function that replaces every second word in a sentence, it takes the word as the default second argument 
# which can be overwritten if there a second argument is passed when the function is called
def replace_second_word(sentence, sub = "Hello"):
    modified_sentence = ""
    count = 0
    for word in sentence.split():
        count += 1
        if (count % 2 != 0):
            modified_sentence += word + " "
        else:
            modified_sentence += sub + " "
    return modified_sentence.strip()

# Printing the days of the week function
print(days_of_week())

# Taking user input to pass into the replace_second_word function
user_sentence = input("\nType in a sentence: ")

print("\nPrinting replace_second_word with default arguments\n")
print(replace_second_word(user_sentence))

print ("\n\nPrinting replace_second_word with the second argument overridden\n")
print(replace_second_word(user_sentence, "Goodbye"))


