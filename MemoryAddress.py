# In this python code we will display the memory location of a variable


your_name = "Karim"
your_age = 23

print(f"The memory address of the variable, 'your_name' is {id(your_name)}")
print(f"The memory address of the variable, 'your_age' is {id(your_age)}")


# Multiple assignment

a = b = c = 2  # all the variables a, b, c indicate the same memory location

print("Address of a = " + str(id(a)))
print("Address of b = " + str(id(b)))
print("Address of c = " + str(id(c)))

