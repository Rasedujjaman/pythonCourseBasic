# This python program is compiled with python 3.7.9

# Here we will learn how to use if-else conditioning

today = 'Saturday'
# today = 'Saturdayyyyy'

day_of_week = {1:'Monday', 2:'Tuesday', 3:'Wednesda', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}


if(day_of_week[1] == today):
     print(f"Today is {day_of_week[1]}")
elif(day_of_week[2] == today):
    print(f"Today is {day_of_week[2]}")
elif(day_of_week[3] == today):
    print(f"Today is {day_of_week[3]}")
elif(day_of_week[4] == today):
    print(f"Today is {day_of_week[4]}")
elif(day_of_week[5] == today):
    print(f"Today is {day_of_week[5]}")     
elif(day_of_week[6] == today):
    print(f"Today is {day_of_week[6]}")
elif(day_of_week[7] == today):
    print(f"Today is {day_of_week[7]}")
    
else:
    print(f"Input is wrong, Check")



# Compact way to write the above code
isFound = 0;
for ii in range(1, 8):
    if(day_of_week[ii] == today):
        print(f"Today is {day_of_week[ii]}")
        isFound = 1;
    elif((ii + 1) == 8 and isFound == 0):
        print(f"Input is wrong, Check")
        