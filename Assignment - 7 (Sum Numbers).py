# 💡 Objective :
# To improve your defining function and arbitrary keyword argument skills.

# Define a function named my_sum to return the sum of all int type inputted numbers.

def my_sum(*ls):
    total = 0
    for i in ls:
        total += i
    return total

# tests

print(my_sum(9, 1, 3, 0, -1))
print(my_sum(5, 7, 4))
print(my_sum(10, -20, 30, 40))