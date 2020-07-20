# Write a code to calculate factorial of a number entered by user.

num = int(input('Enter a number : '))
factorial = 1
for i in range(1,num+1):
    factorial *= i
print(f'{num}! = {factorial}')