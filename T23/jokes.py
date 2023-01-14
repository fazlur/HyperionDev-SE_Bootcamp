# Importing Random Module
import random
# Creating a list of jokes
jokes_list = ["What kind of exercise do lazy people do? Diddly-squats.", "What do you call a pony with a cough? A little horse!", "What is Forrest Gump's password? 1Forrest1.",
    "Why did the M&M go to school? He wanted to be a Smartie.", "What did one traffic light say to the other? Stop looking at me, I'm changing!", "What do you call bears with no ears? B.",
    "What's a foot long and slippery? A slipper!", "What's red and moves up and down? A tomato in an elevator!", "I invented a new word today: Plagiarism.",
    "How does a rabbi make coffee? Hebrews it!", "Rest in peace boiling water. You will be mist!", "Why don't scientists trust atoms? Because they make up everything!"]

# Using random's coice method with the list to print a random joke from the list
print(random.choice(jokes_list))

