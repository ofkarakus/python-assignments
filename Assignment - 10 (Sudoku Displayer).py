# 💡Objective:
# To improve your control flow statement skills.

# Task: The department you work for has received a project that displays the solved sudoku puzzles in a 
# digital environment. 

# Write a Python code to print out the given sudoku puzzle matrix in the following format.

# Given format :
# sudoku = [
#     [0, 0, 0, 0, 6, 4, 0, 0, 0],
#     [7, 0, 0, 0, 0, 0, 3, 9, 0],
#     [8, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 5, 0, 2, 0, 6, 0],
#     [0, 8, 0, 4, 0, 0, 0, 0, 0],
#     [3, 5, 0, 6, 0, 0, 0, 7, 0],
#     [0, 0, 2, 0, 0, 0, 1, 0, 3],
#     [0, 0, 1, 0, 5, 9, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 7, 0, 0]
# ]
# Desired output format :
# - - - - - - - - - - - - - - - 
# 0  0  0  | 0  6  4  | 0  0  0  
# 7  0  0  | 0  0  0  | 3  9  0  
# 8  0  0  | 0  0  0  | 0  0  0  
# - - - - - - - - - - - - - - - 
# 0  0  0  | 5  0  2  | 0  6  0  
# 0  8  0  | 4  0  0  | 0  0  0  
# 3  5  0  | 6  0  0  | 0  7  0  
# - - - - - - - - - - - - - - - 
# 0  0  2  | 0  0  0  | 1  0  3  
# 0  0  1  | 0  5  9  | 0  0  0  
# 0  0  0  | 0  0  0  | 7  0  0  
# - - - - - - - - - - - - - - -

sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

for i in sudoku:
    i.insert(3, '|')
    i.insert(7, '|')
    if sudoku.index(i) % 3 == 0:
        print('- '* 16)
        print(*i, sep='  ')
    else:
        print(*i, sep='  ')
else: print('- '* 16)