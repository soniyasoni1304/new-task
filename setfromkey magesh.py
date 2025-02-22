
# setdefault() is used to check if a key exists in the dictionary and to set it with a default value if it doesn’t.

# Example 1: Key exists
# my_dict = {'a': 10, 'b': 20}
# print(my_dict.setdefault('a', 30))  
# print(my_dict) 

# Example 2: Key doesn't exist
# print(my_dict.setdefault('c', 30))  
# print(my_dict)  

# fromkeys() is used to create a new dictionary with a set of keys, all initialized to the same default value.

# Example 1: With default value of None
# keys = ['a', 'b', 'c']
# my_dict = dict.fromkeys(keys)
# print(my_dict)  

# Example 2: With a custom default value
# my_dict = dict.fromkeys(keys, 10)
# print(my_dict)  