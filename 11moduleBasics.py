# A module allows you to logically organize your Python code.
# Grouping related code into a module makes the code easier to
# understand and use.
# A module is a Python object with arbitrarily named attributes
# that you can bind and reference.
# 
# Simply, a module is a file consisting of Python code.
# A module can define functions, classes and variables.
# A module can also include runnable code.


import math
content_math = dir(math)
print(content_math) # display the contents of the module math


print(math.pi) # display the value of pi
print(math.pow(2,3))  # calculate 2^3
print(math.factorial(5))  # calculate the factorial

# import numpy
# print(dir(numpy))


#Note: the above module math and numpy are provided by python
# we can build our own module