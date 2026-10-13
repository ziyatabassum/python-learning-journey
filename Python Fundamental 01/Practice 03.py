#Ask the user to enter two integers and one float. Convert them all to floats and print their average.

num1 = int(input("Type your 1st int num: "))
num2 = int(input("Type your 2nd int num: "))
num3 = float(input("Type your float num: "))

num1 = float(num1)
num2 = float(num2)

print(f"1st int num to float: {num1}")
print(f"2nd int num to float: {num2}")
print(f"The exinting float num: {num3}")

avarage = (num1 + num2 + num3) / 3
print(f"avarage is = {avarage}")
