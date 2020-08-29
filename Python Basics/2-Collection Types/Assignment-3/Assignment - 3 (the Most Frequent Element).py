# Task : Find out the most frequent number and its frequency.

# Write a program that;

# Finds out the most frequent number in the given list.
# Calculates its frequency.
# Prints out the result.
	
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3, 4, 6, 9, 2, 23, 452, 100, 34, 45, 67, 34, 56, 67, 87, 45, 34, 34, 54]
num = max(numbers, key = numbers.count)
frequency = numbers.count(num)
print(f'the most frequent number is {num} and it was {frequency} times repeated')