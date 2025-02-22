'''import math
print(math.sqrt(16))
print(math.factorial(5))'''


'''import datetime

# 1. Get current date and time
current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

# 2. Get current date
current_date = datetime.date.today()
print("Current Date:", current_date)

# 3. Get current time
current_time = datetime.datetime.now().time()
print("Current Time:", current_time)

# 4. Format the date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted_datetime)

# 5. Creating a specific datetime object
specific_datetime = datetime.datetime(2024, 11, 28, 15, 30, 0)
print("Specific Date and Time:", specific_datetime)

# 6. Parse a string into a datetime object
date_string = "2024-11-28 15:30:00"
parsed_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed Date and Time:", parsed_datetime)

# 7. Timedelta example (difference between two dates)
time_difference = current_datetime - specific_datetime
print("Time Difference:", time_difference)

# 8. Adding/subtracting time using timedelta
one_week = datetime.timedelta(weeks=-1)
new_date = current_datetime + one_week
print("One week from now:", new_date)'''

# random Module

import random

# 1. Generate a random integer between a specified range
random_int = random.randint(1, 5)  # Returns an integer between 1 and 5
print("Random Integer:", random_int)

# 2. Randomly choose an element from a list
random_choice = random.choice(['apple', 'banana', 'cherry', 'date'])
print("Random Choice from List:", random_choice)

random_step = random.randrange(0, 10, 2)
print("Random Number with Step Size:", random_step)


