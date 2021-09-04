# Here we will learn how to define and use function in python


# A function is a block of organized, reusable code that is
# used to perform a single, related action. Functions provide
# better modularity for your application and a high degree of
# code reusing.

# Assume that you want to calculate the factorial of a natural number
# We define a function that will calculate the factorial

def my_factorial(num):
    result = 1
    for ii in range(1, num+1):
        result = result*ii
    print(f"The factorial of {num} is {result}")


# Another function that will calculate the summation of (1 to N)
def my_summation(num):
    result = 0
    N = num
    while(N >= 1):
        result = result + N
        N = N - 1
    print(f"The summation of {1} to {num} is {result}")




# Take the user input from the keyboard
number = int(input("Give a positive number: ")) # prompt to take input number

# Calling the function 
my_factorial(number) # calculate the factorial and display the result
my_summation(number) # calculate the summation and display the results


### Note: 
# In the above code my_factorial(arg) and my_summation(arg)
# are user-defined functions, Whereas print(arg) is a built in
# function 
