# Task : Write a program that takes a number from the user and prints the result to check if it is a prime 
# number.

num = int(input('Enter a number : '))
i = 2

if num == 2:
    status = f'{num} is a prime number'
elif num < 2:
    status = f'{num} is not a prime number'
else:
    while num % i != 0 and i < num:
        status = f'{num} is a prime number'
        i += 1
    while num % i == 0 and i < num:
        status = f'{num} is not a prime number'
        i += 1

print(status)