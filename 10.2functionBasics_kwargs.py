# Here we well learn how to pass a dictionary type arguments in a function
# kwargs stands for keyword arguments


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
# *args and **kwargs are used to define functions that take a varying number of input arguments. 
# the single asterisk operator * can be used on any iterable that python provides, i.e. list, tupple etc, 
# while the double asterisk operator ** can only be used on dictionaries. 

# The correct order of arguments while difining the function
#  def my_function(a, b, *args, **kwargs):
#      pass 




