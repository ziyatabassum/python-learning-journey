'''Take a decimal number as input (like 45.78 ) and output its:
    • integer part - 45
    • fractional part - .78'''

num = float(input("Enter a decimal num: "))

part_1 = int(num)
part_2 = num - part_1

print(f"{num}'s\n • integer part - {part_1}\n • fractional part - {part_2:.2f}")