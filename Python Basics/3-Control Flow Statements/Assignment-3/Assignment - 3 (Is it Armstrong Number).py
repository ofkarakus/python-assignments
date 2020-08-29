# Task:

# Find out if a given number is an "Armstrong Number".

# An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number. 

# Examples :
# 371 = 3**3 + 7**3 + 1**3;
# 9474 = 9**4 + 4**4 + 7**4 + 4**4;

# Write a Python program that;
# takes a positive integer number from the user,
# checks the entered number if it is Armstrong,
# consider the negative, float and any entries other than numeric values then display a warning message to 
# the user.


number = input('Please enter a number : ').strip()

if not number.isdigit() or int(number) < 0:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
else:
    total = 0
    for i in number:
        total += int(i) ** len(number)
    if int(number) == total:
        print(f'{number} is an Armstrong number')
    else:
        print(f'{number} is not an Armstrong number')