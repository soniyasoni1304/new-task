# main.py

from mypackage import math_operations, string_operations

# Using functions from math_operations module
result = math_operations.add(10, 5)
print("Addition of a and b is: ",result) 

# Using functions from string_operations module
concatenated = string_operations.concatenate("Welcome to", " Tamtree")
print("String concodination:  ",concatenated)  

lenth_str=string_operations.length(str(len("Tamtree")))
print("Length of the string is: ",lenth_str)

