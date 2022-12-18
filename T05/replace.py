#Original string from Task 2
single_string = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

#Using the replace method to replace the exclamation marks with spaces
print (single_string.replace("!", " "))

"""
Adding the upper() method to convert the string to upper case
after the replace method which is replacing the exclamation 
marks with spaces
"""

print(single_string.replace("!", " ").upper())

#Using slice without start or end to include all of the string, but setting the step to -1 to step backwards
print(single_string.replace("!", " ")[::-1])