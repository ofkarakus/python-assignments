# 💡 Objective :
# To improve your defining function and arbitrary keyword argument skills.

# Define a function named my_min to find the min of the inputted numbers.

def my_min(*num):
    minimum = num[0]
    for i in num:
        if i < minimum:
            minimum = i
    return minimum

# Tests

print(my_min(5,6,7))
print(my_min(3,8,-9,0,12,1.2,-79))
print(my_min(-100))