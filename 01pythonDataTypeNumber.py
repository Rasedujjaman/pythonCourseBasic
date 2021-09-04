# There are five standard data types in python

#01: Numbers
#02: String
#03: List
#04: Tuple
#05: Dictionary


########################################################################
########################################################################
## Here we will discuss about Numbers

## Python supports four different numerical data type, Namely

# int (signed intergers)
# long (long integers)
# float (floating point real values)
# complex( complex numbers)

## Examples: 
your_age = 23; # int type
your_cgpa = 3.51 # float type
z1 = 3.5 + 6j # complex type

# display the type 
print(type(your_age))
print(type(your_cgpa))
print(type(z1))

# Doing operation on complex number
z2 = 5 + 9j
print(f"z1 = {z1}")
print(f"z2 = {z2}")
print(f"z1 + z2 = {z1+z2}") # Addition of two complex numbers

z3 = complex(4, -9) # Another way to make complex number
print(f"z3 = {z3}")
print(f"Real part of z3 = {z3.real}")      # display the real part of the complex number
print(f"Imaginary part of z3 = {z3.imag}") # display the imaginary part of the complex number


# Delete a variable or multiple variable

print(f"The address of {z1} is {hex(id(z1))}")
print(f"The address of {z2} is {hex(id(z2))}")
print(f"The address of {z3} is {hex(id(z3))}")
del z1, z2, z3  # All three variables z1, z2 and z3 are deleted
# print(f"The address of {z1} is {hex(id(z1))}") # Invalid operatoin

# Converting type
print(your_cgpa)
print(int(your_cgpa)) # Converting into integer type
print(complex(your_cgpa)) # Converting into complex form float type

# Converting into absolute value
print(abs(your_cgpa))
print(abs(-100))





