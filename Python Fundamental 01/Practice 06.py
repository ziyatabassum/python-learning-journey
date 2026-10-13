#Write a program to swap values of two numbers entered by the user

num1 = input("Enter num1: ")
num2 = input("Enter num2: ")

place_holder = num1
num1 = num2
num2 = place_holder

print(f"After swapping,\n num1 = {num1}\n num2 = {num2}")