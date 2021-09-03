# Here we will learn python list

# List are similar to array in C++ but in list we can put any data type 
# A python list contain items separated by commas and enclosed within squre
# brackets([])


my_list = ['abcd', 333, 2.33, 'Karim', 70];

my_list2 = ['Saha Alam', 3.44, 89]

print(my_list)      # print the entire list (my_list)
print(my_list[0])   # print the first element of the list

my_list[0] = 'efgh' # modify the first element of my_list
print(my_list[0])

print(my_list[2:4]) # print the third and fourth element of the list
# note: python indexing starts from 0 
# in the example: my_list[2:4] --> this will display the third and fourth element only. The upper limit 4 is excluded.

print(my_list[2:]) # prints all the elements starting from 3rd element

print(my_list2 * 2)   # Print my_list2 two times



# List concatenation 

print(my_list + my_list2)    
