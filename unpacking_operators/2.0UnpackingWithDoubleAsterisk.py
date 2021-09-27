# The unpacking operators are operators that unpack the values from
# iterable objects (i.e. list, tuples, dictionary etc) in python.
# the single asterisk operator * can be used on any iterable that Python provides
# the double asterisk operator ** can only be used on dictionaries


food_items = {'fish':3, 'meat':5, 'pasta':9} 

# Unfortunately, we can’t unpack a dictionary to a single variable as we’ve been
# doing with tuples and lists. That means the following will throw an error:
# print(**food_items)  # this will throw errors

# But we can perform other operatios like merging two dictionaries
food_fruits = {'apples': 2, 'oranges': 4}

# We can perform the merge operation very easily with double asterisks
merged_dict = {**food_items, **food_fruits}

print(merged_dict) # Here we will see a merged dictionary

