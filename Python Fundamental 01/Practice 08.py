'''Take the radius (r) as user input and print the area.
Use the formula: Area = π * r^2 (value of π = 3.14)'''

import math 

radius = float(input("Enter the circle's radius: "))
Area = math.pi * radius ** 2

print("Area is = ",Area)