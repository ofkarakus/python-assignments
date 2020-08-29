# Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.

# The desired output is like :
# fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

fibonacci_nums = []

first = 0
second = 1
last = 1

while last < 56:
    fibonacci_nums.append(last)
    last = first + second
    first = second
    second = last

print(fibonacci_nums)