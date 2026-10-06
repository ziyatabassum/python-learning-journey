''' A variable is like a container that stores data or values in our program. We can
think of it as a labeled box that we can put something in, change it or use it later.
The variables in Python have names called identifiers, can store data of any type '''

name = "Tabassum Zia Prova" 
age = 23 
PI = 3.14 
Interest_in = "Arificial Intelligence" 

print(name)
print("She's", age, "years old.")
print (PI)
print("Her interest is in", Interest_in)
print("Her name is", name, "and she is", age, "years old. Her interest is in", Interest_in, "and the value of PI is", PI)
print("Her name is {} and she is {} years old. Her interest is in {} and the value of PI is {}".format(name, age, Interest_in, PI))
print(f"Her name is {name} and she is {age} years old. Her interest is in {Interest_in} and the value of PI is {PI}")
print("Her name is %s and she is %d years old. Her interest is in %s and the value of PI is %.2f" %(name, age, Interest_in, PI))
print("Her name is {0} and she is {1} years old. Her interest is in {2} and the value of PI is {3}".format(name, age, Interest_in, PI))
print("Her name is {name} and she is {age} years old. Her interest is in {Interest_in} and the value of PI is {PI}".format(name=name, age=age, Interest_in=Interest_in, PI=PI))
print("Her name is {name} and she is {age} years old. Her interest is in {Interest_in} and the value of PI is {PI}".format_map(vars()))
print("Her name is {name} and she is {age} years old. Her interest is in {Interest_in} and the value of PI is {PI}".format_map(locals()))
print("Her name is {name} and she is {age} years old. Her interest is in {Interest_in} and the value of PI is {PI}".format_map(globals()))