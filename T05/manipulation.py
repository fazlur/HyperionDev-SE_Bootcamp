
#Getting input from user
str_manip = input("Write a sentence: ")


#Printing out the length of the string by using the string length (len) method
print(f"The length of the string is {len(str_manip)}")


"""
Finding the last letter in the string by using string indexes
and passing it as the character to be replaced by (first argument)
of the replace method then passing "@" as the replacement character 
(second argument) of the replace method 
"""
print(str_manip.replace(str_manip[-1], "@"))


"""
Printing the last 3 characters backwards by setting the last 3 characters (-4)
as the stop value of the slice, and then using -1 as the step value for the 
backwards stepping of the string
"""
print(f"Printing the last 3 characters backwards: {str_manip[:-4:-1]}")


"""
Creating a five letter word by using slicing to get the first 3 characters of the 
word and concatenating it with the result of a slice that takes the start point
as the last 2 characters and foes to the end of the string
"""
print(f"The five letter word: {str_manip[:3]}{str_manip[-2:]}")