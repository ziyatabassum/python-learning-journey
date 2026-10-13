'''The user enters a string containing a number (e.g., "45" ). Convert it to:
• an integer
• a float
• a string again
Print all three values with their types.'''

#if str contains decimal point num, then it will show error
string = str(input("Enter your string: "))

integer = int(string)
print(f"from {string} as str Converted to int: {integer} {type(integer)}")

floating = float(string)
print(f"from {string} as str Converted to float: {floating} {type(floating)}")

string_again = str(integer)
print(f"from {integer} as int Converted to str again: {string_again} {type(string_again)}")

string_again = str(floating)
print(f"from {floating} as float Converted to str again: {string_again} {type(string_again)}")

