# Here we will try  to understand the string data type in python


text = "Hello how are you?" 
print(text)

print(text[0]) # print the first character of text
print(text[-1]) # print the last chracter of text


print(text[-12:-1])
print(text[6:-1])
print(text[6:])   # prints string starting from the 7th character
print(text[-12:]) # prints string strating from the 7th character as well

print(text.upper()) # this will convert the string into upper case
print(len(text))   # this will display the number of characters in the string
print(text.lower()) # this will convert the stirng into lower case

# Count how many o in text
print(text.count("o"))

# We can also count entire words, that occurs in the string

s = "I have had so many cats that had so namy kids that had beautiful eyes"
print(s)
print(f"There are {s.count('had')} had in the above string")

# Replace eyes in the above string to nose

print(s.replace("eye", "nose"))


