# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

animal = "Lion" # Added quotes around the string "Lion" to avoid a run time error
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth" # Added the f before the string so the variables could be interpreted
                                                                                            # and swapped the order of number_of_teeth with animal_type otherwise
                                                                                            # the sentence doesn't make sense, causing a logical error

print (full_spec) # Added the parenthesis around the variable to avoid a Syntax error

