# Task-1:
# Write a short Python program that asks the user to enter Celsius temperature 
# (it can be a decimal number), converts the entered temperature into Fahrenheit degree 
# and prints the result.

# Task-2:
# Write a short Python program that asks the user to enter a distance 
# (it can be a decimal number) in kilometers, converts the entered distance into miles 
# and prints the result.

# Task-1
celcius = input('Enter a temperature in celcius, please: ')
celcius = float(celcius)
fahrenheit = (celcius * 9 / 5) + 32
print(celcius, 'celcius =', fahrenheit, 'fahrenheit', '\n')

# Task-2
km = input('Enter a distance in kilometers, please: ')
km = float(km)
miles = km / 1.60934
print(km, 'kilometers =', miles, 'miles')