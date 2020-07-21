# Define a “function” to calculate permutation of 2 numbers.
# Reminder: P(n,r) = n!/(n-r)!
# Clue: Defining a function that calculates factorial of given number, may be 
# helpful.

def factorial(x):
    fact = 1
    for i in range(1, x+1):
        fact *= i
    return fact


def permutation(n,r):
    return factorial(n) / factorial(n-r)

# tests

print(permutation(5,0))
print(permutation(5,1))
print(permutation(5,2))
print(permutation(5,3))
print(permutation(5,4))
print(permutation(5,5))