# Here we will learn how to define and use function that will accept any number of
# numerical data (int, float) and return the summation of those numbers

# Problem statement: we know how to accept two numbers as
# arguments and return the summation, now if we want to add
# more than two numbers how can we do it?


# See the code below to find the answer of the above question



# Another function that will calculate the summation of two or more numbers
def my_summation(*args):
    summation = 0
    
    # args: is a place holder for any number of argumnets
    # print(args) # it displays all the argumnets as a tupple
    
    for i in args:
        summation = summation + i
    
    print(f"The summation is: {summation}")
    
    
# Calling the function
my_summation(20, 20) # calculate the summation of two numbers
my_summation(30, 12, 60)  # calculate the summation of three numbers
my_summation(12, 32, 23, 44, 30, 100) # calculate the summation and display the results


### Note: 
# We have designed the my_summation function in such a way
# it can accept any number of argumnents and find the summations
