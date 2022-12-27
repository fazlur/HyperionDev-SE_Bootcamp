# List holding friend's names
friends_names = ["Bruce Lee", "Mike Tyson", "Tupac Shakur"]

# Printing out name of 1st and last friend in the list
print(f"My first friend in the list is: {friends_names[0]}")
print(f"My last friend in the list is: {friends_names[-1]}")

# List holding the age of friends
friends_ages = [82, 56, 49] 



# NOT ASKED IN EXERCISE - DONE FOR PRACTICE
# Looping through the lists and printing values in same position

for i in range(len(friends_names)):
    print(f"It has been {friends_ages[i]} years since {friends_names[i]} was born!")