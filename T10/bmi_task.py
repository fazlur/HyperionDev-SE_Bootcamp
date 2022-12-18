#Getting the user's height and weight
weight = float(input("Type in your weight in KG: "))
height = float(input("What is your height in meters: "))

#Calculating the BMI
bmi = round(weight / ((height) * (height)),2)

#Outputing to the user their BMI and classification
if(bmi >= 30):
  print(f"Your current BMI is {bmi}, with that BMI you are classed as obese.")
elif(bmi >= 25):
  print(f"Your current BMI is {bmi}, with that BMI you are classed as overweight.")
elif(bmi >= 18.5):
  print(f"Your current BMI is {bmi}, with that BMI you are classed as normal.")
else:
  print(f"Your current BMI is {bmi}, with that BMI you are classed as underweight.")