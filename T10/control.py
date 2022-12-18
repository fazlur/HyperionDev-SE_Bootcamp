#Getting the user's age
age = int(input("Type in your age in numbers: "))
#First checking if the user is 18 or older, if not checking if he is older than 16 otherwise printing that user is too young
if (age >= 18):
  print("You are old enough!")
elif (age > 16):
  print("Almost there")
else:
  print("You're just too young!")