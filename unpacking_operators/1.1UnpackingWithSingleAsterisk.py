# The unpacking operators are operators that unpack the values from
# iterable objects in python.
# the single asterisk operator * can be used on any iterable that Python provides
#  while the double asterisk operator ** can only be used on dictionaries

def my_sum(a, b, c):
    print(a+b+c)





my_list = [1, 3, 4]

my_list1 = [2, 3, 4, 5]
my_sum(*my_list) # my_list must have the same number of arguments as of the my_sum function

my_sum(*my_list1) # throws errors because of mismatch of number of elements in my_list1 and required arguments of my_sum function  



