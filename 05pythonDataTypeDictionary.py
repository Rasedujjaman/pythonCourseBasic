# Python dictionaries works like associative arrays and
# consists of key-value pairs.

# A dictionary key can be any python data type but are 
# usually numbers and strings. The values can be any data type

# Dictionaries are enclosed by curly braces ({}) and values can be 
# assigned and accessed using squre braces([]). 

dictionary1 = {'name': 'Karim', 'age': 23, 'cgpa': 3.56}

print(dictionary1) # print the entire dictionary

print(dictionary1.keys()) # display all the keys
print(dictionary1.values()) # display all the values 

print(f"Name : {dictionary1['name']}")
print(f"Age : {dictionary1['age']}")
print(f"CGPA : {dictionary1['cgpa']}")


# Function with Description
print(len(dictionary1))  # print the length of the dictionary

# Python dictionary method str() produces a printable string representation of a dictionary.
print(str(dictionary1))

# Print the type of the variable
print(type(dictionary1))


# dict.items()
print(dictionary1.items())  