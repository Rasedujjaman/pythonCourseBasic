
# Writing on the file
fileID = open("test.txt", "w") # open a file by the name text.txt
fileID.write("python is a great language")
fileID.close()  #Close opend file


# Reading from the file
fileID = open("test.txt", "r") # Open the file in reading modes
output_string = fileID.read()
print(output_string)
fileID.close()  #Close opend file



#####################################################################
#####################################################################
# Another example here we will write the content of math module in
# a text file

import math

content_math = dir(math)
print(type(content_math))
# Convert the list into string
# using list comprehension
listToStr = ', '.join([str(elem) for elem in content_math])

# Writing to the file
fileID = open("math_dir.txt", "w")
fileID.write(listToStr)
fileID.close()

# Reading form the file
fileID = open("math_dir.txt", "r")
result = fileID.read()
print(result)


####################################################################
####################################################################