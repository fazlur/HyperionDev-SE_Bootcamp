# Reading the input string from the userto check if palindrome
user_word = input("Type in a word : ")
# Reversing the input
reversed_input = user_word[::-1]

#comparing the strings
if user_word == reversed_input:
    print("your word is a palindrome.")
    print(f"{user_word} still reads as {reversed_input}.")
else:
    print("your word is not a palindrome.")
    print(f"{user_word} reversed reads as {reversed_input}.")
