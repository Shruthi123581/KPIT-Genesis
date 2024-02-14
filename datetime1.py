
'''from datetime import *
import pytz


tz_INDIA = pytz.timezone('Asia/Kolkata')
datetime_INDIA = datetime.now(tz_INDIA)
print("INDIA time:", datetime_INDIA.strftime("%H:%M:%S"))
--------------------------------------------
# Getting current date and time using now().

# importing datetime module for now()
import datetime

# using now() to get current time
current_time = datetime.datetime.now()

# Printing value of now.
print("Time now at greenwich meridian is:", current_time)
------------------------------------------------------

# Python program to find yesterday,
# today and tomorrow


# Import datetime and timedelta
# class from datetime module
from datetime import datetime, timedelta


# Get today's date
presentday = datetime.now() # or presentday = datetime.today()

# Get Yesterday
yesterday = presentday - timedelta(1)

# Get Tomorrow
tomorrow = presentday + timedelta(1)


# strftime() is to format date according to
# the need by converting them to string
print("Yesterday = ", yesterday.strftime('%d-%m-%Y'))
print("Today = ", presentday.strftime('%d-%m-%Y'))
print("Tomorrow = ", tomorrow.strftime('%d-%m-%Y'))
------------------------------------------------------
# Python program to convert time 
# from 12 hour to 24 hour format 

# Function to convert the date format 
def convert24(str1): 
	
	# Checking if last two elements of time 
	# is AM and first two elements are 12 
	if str1[-2:] == "AM" and str1[:2] == "12": 
		return "00" + str1[2:-2] 
		
	# remove the AM	 
	elif str1[-2:] == "AM": 
		return str1[:-2] 
	
	# Checking if last two elements of time 
	# is PM and first two elements are 12 
	elif str1[-2:] == "PM" and str1[:2] == "12": 
		return str1[:-2] 
		
	else: 
		
		# add 12 to hours and remove PM 
		return str(int(str1[:2]) + 12) + str1[2:8] 

# Driver Code		 
print(convert24("08:05:45 PM")) 
----------------------------------
# Python program to find the
# difference between two times


# function to obtain the time
# in minutes form
def difference(h1, m1, h2, m2):
	
	# convert h1 : m1 into
	# minutes
	t1 = h1 * 60 + m1
	
	# convert h2 : m2 into
	# minutes
	t2 = h2 * 60 + m2
	
	if (t1 == t2):
		print("Both are same times")
		return
	else:
		
		# calculating the difference
		diff = t2-t1
		
	# calculating hours from
	# difference
	h = (int(diff / 60)) % 24
	
	# calculating minutes from
	# difference
	m = diff % 60

	print(h, ":", m)

# Driver's code
if __name__ == "__main__":
	
	difference(7, 20, 9, 45)
	difference(15, 23, 18, 54)
	difference(16, 20, 16, 20)

# This code is contributed by SrujayReddy
-------------------------------------------

# python program Find number of
# times every day occurs in a Year 


import datetime 
import calendar

def day_occur_time(year):
	
	# stores days in a week 
	days = [ "Monday", "Tuesday", "Wednesday", 
		"Thursday", "Friday", "Saturday", 
		"Sunday" ]
	
	# Initialize all counts as 52
	L = [52 for i in range(7)]
	
	# Find the index of the first day
	# of the year
	pos = -1
	day = datetime.datetime(year, month = 1, day = 1).strftime("%A")
	for i in range(7):
		if day == days[i]:
			pos = i
			
	# mark the occurrence to be 53 of 1st day
	# and 2nd day if the year is leap year
	if calendar.isleap(year):
		L[pos] += 1
		L[(pos+1)%7] += 1
		
	else:
		L[pos] += 1
		
	
	# Print the days
	for i in range(7):
		print(days[i], L[i])
	

# Driver Code 
year = 2019
day_occur_time(year)
--------------------------------

'''
