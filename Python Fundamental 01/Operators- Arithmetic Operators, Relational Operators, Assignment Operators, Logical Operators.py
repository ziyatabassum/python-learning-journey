'''An operator is a symbol that tells Python to perform a specific computation on one or more values (called operands).
Example:
There are several types of operators in Python. Let’s start by understanding some of the most common ones:'''

# 1. Arithmetic Operators - used to perform math operations.
# Operators - +, -, *, /, %, **, //

from ast import compare


print(1 + 3)                                                 # '+' is an Operator & (1, 3) are operands
a = 5                                                        # int
b = 10                                                       # int
print(a + b)                                                 # Addition 
print(a - b)                                                 # Subtraction 
print(a * b)                                                 # Multiplication 
print(a / b)                                                 # Division 
print(a % b)                                                 # Modulo - remainder
print(a ** b)                                                # Power

# 2. Relational Operators - used to compare values.
#Operators - ==, !=, >, <, >=, <=

a = 10
b = 20

# Equal to
print("a == b:", a == b) # False

# Not equal to
print("a != b:", a != b) # True

# Greater than
print("a > b:", a > b) # False

# Less than
print("a < b:", a < b) # True

# Greater than or equal to 
print("a >= b:", a >= b) # False 

# Less than or equal to 
print ("a <= b:", a <= b) # True

# 3. Assignment Operators - used to assign values to variables.
# Operators: =, +=, -=, *=, /=, %=, **=

a = 10
b = 20

# Equal to
print("a == b:", a == b)                            # False

# Not equal to
print("a != b:", a != b)                            # True

# Greater than
print("a > b:", a > b)                              # False

# Less than
print("a < b:", a < b)                              # True

# Greater than or equal to 
print("a >= b:", a >= b)                            # False 

# Less than or equal to 
print ("a <= b:", a <= b)                            # True

# Simple assignment
x = 10
print("x =", x)                                    # 10

x += 5 # equivalent to x = x + 5
print("x += 5 ->", x)                              # 15

x -= 3 # equivalent to x = x - 3
print("x -= 3 ->", x)                              # 12

x *= 2 # equivalent to x = x * 2
print("x *= 2 ->", x)                              # 24 

x /= 4 # equivalent to x = x / 4 
print("x /= 4 ->", x)                              # 6.0 

x %= 4 # equivalent to x = x % 4 
print("x %= 4 ->", x)                              # 2.0 

x **= 3 # equivalent to x = x ** 3 
print("x **= 3 ->", x)                              # 8.0

# 4. Logical Operators - used to combine conditional statements. used to combine boolean values.
# Operators: and, or, not

a = True
b = False

print("a and b:", a and b)                         # False
print("a or b:", a or b)                           # True
print("not a:", not a)                             # False

x = 10 
y = 20 
z = 5 
# AND 
print(x > z and y > x)                             # True 
# OR 
print(x > y or y > z)                              # True 
# NOT 
print(not (x > y))                                 # True

'''Operator Precendence
Operators have a priority i.e there is a specific order in which operations are to be 
performed in case we have multiple operators in the same expression. The order is 
as follows:
• ()- Parentheses (highest priority)
• **- Exponent
• +x, -x, ~x - Unary operators
• *, /, //, % - Multiplication, division, floor, modulus
• +, - - Addition, subtraction
• <<, >> - Bitwise shifts
• & - Bitwise AND
• ^ - Bitwise XOR
• | - Bitwise OR
• Comparison operators - <, <=, >, >=, !=, ==
• not
• and
• or
• Assignment operators - =, +=, -= ... '''

'''Note - Unary operators are operators that works on a single operand
(a single value or variable) to perform an operation. These are like , 
 (unary plus), (unary minus) etc. +x is used to indicate positive value & -x is used to indicate negative value.'''

x= 5
y= -x                                 #unary minus
print(x)                              # 5
print(y)                              # -5

# We don’t generally use +x as numbers are positive by default.


'''Input
We use the function to take input from user while the program is running. 
Whatever the user types in input prompt is returned as a string. Syntax:'''

name = input("enter name: ") 
print(name) 
print(type(name)) # type is string

'''We can use type conversion functions to convert the type of input.'''

# program to add 2 numbers entered by the user 
a = int(input("enter 1st num: ")) 
b = int(input("enter 2nd num: ")) 

print(a + b)

'''Let’s summarize all the concepts we learnt in this chapter into a simple practice 
problem.
Write a program that takes in 2 numbers ( a & b ) and print the average.'''

a = int(input("enter 1st num: "))                    # 5
b = int(input("enter 2nd num: "))                    # 10

avg = (a + b) / 2

print("average = ", avg)                             # 7.5