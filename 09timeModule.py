
import time;  # This is required to include time module.

ticks = time.time()
print (f"Number of ticks since 12:00am, January 1, 1970: {ticks}")

localtime = time.localtime(time.time())
print(f"Local current time : {localtime}")


localtime = time.asctime( time.localtime(time.time()) )
print(f"Local current time : {localtime}")
print("-----------------------------------------------")

####################################################################
# Calender module
import calendar
cal = calendar.month(2021, 9)
print(cal)

print(calendar.isleap(2020))  # print if the year is leapyear