# In this pyton code we will understand the for loop


# Note: format of for loop

# for ii in range(1, 11):
#    print(ii) -> this will print 1 upto 10
# indentation is necessary and the uper limit is one less

# Print 1 to 10 natural number
for ii in range(1, 11):
    print(ii)
    

# print all the members of a list
fruits = ['apple', 'ornage', 'banana', 'mango', 'watermelon'];
for ii in fruits:
    print(ii)
    

# Using len() and for loop we can also print the elements of the list fruits
for ii in range (0, len(fruits)):
    print(fruits[ii])
    
    
# Using for loop find the summation of N natural numbers (1 to N numbers)
N = 100
summation = 0
for ii in range(1, N+1):
    summation = summation + ii
print(f"The summation of {1} to {N} is {summation}")


# Using for loop find the factorail of N (N being a natuarla number)
N = 10
factorial = 1
for ii in range(1, N+1):
    factorial = factorial*ii
print(f"The factorial of {N} is {factorial}")
