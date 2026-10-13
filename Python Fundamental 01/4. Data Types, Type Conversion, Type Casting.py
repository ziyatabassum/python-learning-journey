'''A data type defines the kind of value a variable can hold. Python has several built-in data types. 
int, float, complex, bool, str, list, tuple, set, dict, etc. are some of the built-in data types in Python.'''

x = 10 
print(type(x))                               # <class 'int'> 

PI = 3.14 
print(type(PI))                              # <class 'float'> 

name = "Prova" 
print(type(name))                            # <class 'str'> 

isTeacher = True
print(type(isTeacher))                       # <class 'bool'>

empty_var = None
print(type(empty_var))                       # <class 'NoneType'>

'''Type conversion is when we convert(cast) variables from one type to another. It can 
happen in 2 ways:'''
# 1. Type Conversion - Implicit, done automatically by Python
a = 5
b = 3.0
print(a + b)                                 # Python converts ans in float by default, so the output will be 8.0
# 2. Type Casting - Explicit, done manually by the programmer
c = float(a)                                 # Converts integer to float
d = int(b)                                   # Converts float to integer
print(c)                                     # Output: 5.0
print(d)                                     # Output: 3