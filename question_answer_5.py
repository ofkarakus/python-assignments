# QUESTION:
# Write a Python code to get lengths of a triangle from a user and then check them 
# whether this triangle is equilateral, isosceles or scalene.

print("Please input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

while not ((x < (y + z)) and x > ((y - z) if (y - z) > 0 else -(y-z))):
    print('You need to input available numbers can create a triangle. Please try again.')
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))

if x == y and x == z:
    print('This triangle is an equilateral triangle.')
elif x == y or x == z or y == z:
    print('This triangle is an isosceles triangle.')
else:
    print('This triangle is a scalene triangle.')