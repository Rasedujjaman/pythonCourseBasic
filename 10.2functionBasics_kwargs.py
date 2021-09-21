# Here we well learn how to pass a dictionary type arguments in a function

def disp_infos(**kwargs): 
    
    
    # kwargs: is a place holder for any number of argumnets as key and value pairs
    print(kwargs) # it displays all the argumnets as a dictionary
    
    for key, value in kwargs.items():
        print(f"Key: {key}, Value: {value}")

    
    
# Different ways to call the function
disp_infos(name="Karim", age = 34, result=3.21)


# Another way to call the function
data = {"name": "Karim", "age": 34, "result":3.21}
disp_infos(**data) # when we pass the dictionary we need to put ** in the argument



### Note: 
# Both ways of calling the function are identical
