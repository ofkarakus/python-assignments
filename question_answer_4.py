# QUESTION:
# Write a Python code to sort the list at below without using .sort() method of list.
# elements of list = [999, 333, 2, 8982, 12, 45, 77, 99, 11]
# Expected output:
# [2, 11, 12, 45, 77, 99, 333, 999, 8982]

ls = [999, 333, 2, 8982, 12, 45, 77, 99, 11]

for i in range(len(ls)):
    for j in range(i+1, len(ls)):
        if ls[i] > ls[j]:
            temp = ls[i]
            ls[i] = ls[j]
            ls[j] = temp
print(ls)