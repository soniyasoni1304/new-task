                              # Creating a dictionary of countries and their capitals
countries = {
    "USA": "Washington, D.C.",
    "Canada": "Ottawa",
    "France": "Paris",
    "Japan": "Tokyo",
    "Japan": "Tokyo"

}

print(countries)


# Dictionary with different types of values
person = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "hobbies": ["reading", "swimming", "traveling"]
}

# print(person)

# The len() function returns the number of key-value pairs in the dictionary
# print(len(countries))

# Accessing value by key
# print(countries["USA"])  
# print(person["name"])


# Using get() to access value (safer, avoids errors if key doesn't exist)
# print(countries.get("France"))  


# Adding a new key-value pair
# countries["Germany"] = "Berlin" 
# print(countries)

# Adding a new key-value pair using update() method
# countries.update({"Russia":"Moscow"})
# print(countries)

# Modifying an existing key-value pair
# countries["USA"] = "New York"  # Change the capital of USA to New York

# print(countries)


# Removing a specific key-value pair using del
# del countries["Canada"]
# print(countries)

# # Removing and returning a specific key-value pair using pop()
# removed_item = countries.pop("Japan")
# print(countries)
# # Removing the last inserted item using popitem()
# last_item = countries.popitem()
# # print(countries)
# print("Removed item:", removed_item)
# print("Last item removed:", last_item)


# # Iterating through dictionary keys
# for country in countries:
#     print(country)

# # Iterating through dictionary values
# for capital in countries.values():
#     print(capital)

# Iterating through dictionary key-value pairs
# for country, capital in countries.items():
#     print(f"The capital of {country} is {capital}.")

# # Using keys(), values(), and items() methods
# print(countries.keys())   
# print(countries.values()) 
# print(countries.items())  

# # Using copy() method
countries.copy()
print(countries)

# Clearing the dictionary
# countries.clear()
# print(countries)  


