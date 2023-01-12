# Original Dictionary
abbreviation_dictionary = {
    'API' : 'Application Programming Interface',
    'IDE' : 'Integrated Development Environment',
    'SDK' : 'Software Development Kit',
    'UI'  :  'User Interface',
    'UX'  : 'User Experience'
}

# Adding two new entries
abbreviation_dictionary['OOP'] = "Object-Oriented Programming"
abbreviation_dictionary['SSH'] = "Secure Shell"

# Asking the user 
user_input = input("What abbreviation would you like to know the meaning: ")

# Program logic
if user_input.upper() in abbreviation_dictionary.keys():
    print(f'''{user_input.upper()}  : {abbreviation_dictionary[user_input.upper()]}''')
else:
    print("Abbreviation not found")


