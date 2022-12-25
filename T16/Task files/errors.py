# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

# Fixed a SyntaxError on line  6, the print was missing the brackets
print ("Welcome to the error program")
# Fixed a SyntaxError and IndentationError on previous line 7 (code below), the print was missing the brackets and was indented
print ("\n")

# The next 6 lines (below) were indented where they didn't have to, the wrong assignment operator "=="
# was used to assign a value to ageStr, and was being passed was a string
ageStr = "24" #I'm 24 years old.
age = int(ageStr) #This initially failed due to a ValueError/ Run time because the value initially assigned to the variable contained characters that could not be casted to INT
print("I'm " + ageStr + " years old.") # changed the variable being concatenated by a String type variable, as concatenation will only be allowed between strings, this triggered a TypeError/ Run time error 
three = "3"

answerYears = age #+ int(three) # I have casted the value ot three to int so the addition could be executed, trying to add between a int(age) and a string (three) triggers a TypeError/ Run time error
                # I have then comment out the addition to the value of variable three as I think this is a logical error, I don't see the purpose of that addition given what the next lines of code try to achieve
#The next 2 prints where missing the brackets, which is a syntax error
print ("The total number of years: " + ageStr) # Replaced the variable answerYears which is a int with ageStr which is a string  to allow the concatenation to happen, this was a logical error
#The first error with the line below was a TypeError/Run time error where a variable was being used without being declared/initialized
answerMonths = (answerYears + int(three)) * 12 + 6 # Added the sums required to give a result in months of the age plus 3 and half years, without that the print below would not be correct, a logical error 
print ("In 3 years and 6 months, I'll be " + str(answerMonths) + " months old") #Casted answerMonths to String to address the TypeError/Run time error caused by trying to concatenate a string with a int type variable

#HINT, 330 months is the correct answer

