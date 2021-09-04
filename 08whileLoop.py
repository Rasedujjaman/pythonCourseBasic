# Here we will learn while loop in python

# while(condition):
#    statements

# Example print 1 to 20 uisng while loop

N = 1
while(N <= 20):
    print(N)
    N = N + 1
    
    
# find the summation of 1 to 100 using while loop
N =  100
summation  = 0  # the initial summation
while(N >= 1):
    summation = summation + N
    N = N - 1
print(f"The summation of {1} to {N} is {summation}")

# Find the factorail of N
N = 10
factorial = 1
while(N >= 1):
    factorial = factorial * N
    N = N - 1
print(f"Factorial of {N} is {factorial}")