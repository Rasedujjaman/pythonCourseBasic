# The unpacking operators are operators that unpack the values from
# iterable objects in python.
# the single asterisk operator * can be used on any iterable that Python provides
#  while the double asterisk operator ** can only be used on dictionaries


# multiple unpacking

def my_sum(*args):
    summation = 0
    for x in args:
        summation += x
    return summation







list1 = [1, 3, 4]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(*list1, *list2, *list3))


# note: here all three lists are unpacked. Each individual item is passed to my_sum() and produce the 
# summation 
# the above call is equivalent to 
print(my_sum(1, 3, 4, 4, 5, 6, 7, 8, 9))
