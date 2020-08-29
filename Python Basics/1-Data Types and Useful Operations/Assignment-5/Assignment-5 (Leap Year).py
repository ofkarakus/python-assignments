# Task:

# Find out if a given year is a "leap" year.

# In the Gregorian calendar, three criteria must be taken into account to identify leap years:
# The year must be evenly divisible by 4;
# If the year can also be evenly divided by 100, it is not a leap year; unless...
# The year is also evenly divisible by 400. Then it is a leap year.
# According to these rules, the years 2000 and 2400 are leap years, 
# while 1800, 1900, 2100, 2200, 2300, and 2500 are not the leap years.

# Write a Python program that;
# Takes a 4-digit year from the user,
# Prints True if the given year by the user is a leap year, prints False otherwise.

leap_year = int(input('year : '))

print(leap_year % 400 == 0 or (leap_year % 4 == 0 and leap_year % 100 != 0))