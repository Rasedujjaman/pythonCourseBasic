# The unpacking operators are operators that unpack the values from
# iterable objects in python.
# the single asterisk operator * can be used on any iterable that Python provides
#  while the double asterisk operator ** can only be used on dictionaries


my_list = [1, 3, 4]

# First print
print(my_list)  # Here the list is directly printed as it was defined



# Second print
print(*my_list) # Here we only see the contents, i.e the * operator tells print() to unpack
# the list first

# In the second print case, the output is no longer the list itself, but the content of the list



