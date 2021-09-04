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
new_list = my_list + my_list2
print(new_list)

print(len(new_list))

# Inserting a new elemet at a particular location
# list.insert(index, obj)
new_list.insert(3, 2001)
print(new_list)

new_list.insert(0, 'Hello')  # insert a new element at the first location 
print(new_list)

# Reverseing the list
new_list.reverse()
print(new_list)

# pop out an element
new_list.pop() # Pop out the last element
print(new_list)

# pop out 5th element
new_list.pop(4)
print(new_list)


# Appending a new element at the end of the list
# list.append(obj)
new_list.append(131)
print(new_list)
