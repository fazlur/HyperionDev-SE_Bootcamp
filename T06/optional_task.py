#Getting the length of each side of the triangle
side1 = float(input("Triangle side 1 length: "))
side2 = float(input("Triangle side 2 length: "))
side3 = float(input("Triangle side 3 length: "))

#Calculating the perimeter of the triangle
perimeter = (side1 + side2 + side3) / 2

#Calculating the area
area = (perimeter*(perimeter - side1)*(perimeter - side2)*(perimeter - side3))**0.5

#Printing out the area using are to limit the result to 2 decimal places
print(f"The are of the triangle is {round(area, 2)}")