# 💡 Objective :
# To improve your defining function and arbitrary keyword argument skills.

# Define a function named my_min to find the min of the inputted numbers.

def my_min(*num):
    temp = num[0]
    for i in num:
        if i < temp:
            temp = i
    return temp