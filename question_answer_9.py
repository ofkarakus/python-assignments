# Write a Python code that finds the students who have maximum and minimum average 
# at a given dictionary below.
# {'Student-1': {'Lesson-1': 57, 'Lesson-2': 46, 'Lesson-3': 58, 'Lesson-4': 81, 
# 'Lesson-5': 85}, 'Student-2': {'Lesson-1': 85, 'Lesson-2': 56, 'Lesson-3': 51, 
# 'Lesson-4': 69, 'Lesson-5': 67}, 'Student-3': {'Lesson-1': 68, 'Lesson-2': 76, 
# 'Lesson-3': 87, 'Lesson-4': 57, 'Lesson-5': 56}, 'Student-4': {'Lesson-1': 78, 
# 'Lesson-2': 93, 'Lesson-3': 88, 'Lesson-4': 38, 'Lesson-5': 54}, 'Student-5': 
# {'Lesson-1': 50, 'Lesson-2': 46, 'Lesson-3': 78, 'Lesson-4': 81, 'Lesson-5': 75}}

students = {
    'Student-1': {'Lesson-1': 57, 'Lesson-2': 46, 'Lesson-3': 58, 'Lesson-4': 81, 'Lesson-5': 85}, 
    'Student-2': {'Lesson-1': 85, 'Lesson-2': 56, 'Lesson-3': 51, 'Lesson-4': 69, 'Lesson-5': 67}, 
    'Student-3': {'Lesson-1': 68, 'Lesson-2': 76, 'Lesson-3': 87, 'Lesson-4': 57, 'Lesson-5': 56}, 
    'Student-4': {'Lesson-1': 78, 'Lesson-2': 93, 'Lesson-3': 88, 'Lesson-4': 38, 'Lesson-5': 54}, 
    'Student-5': {'Lesson-1': 50, 'Lesson-2': 46, 'Lesson-3': 78, 'Lesson-4': 81, 'Lesson-5': 75}
    }

# first answer

max_criterion = 0
min_criterion = 100
average_dict = dict(zip(list(students.keys()), list(map(lambda x : sum(x.values())/len(x.keys()), students.values()))))

for i in average_dict:
    if average_dict[i] > max_criterion:
        max_criterion = average_dict[i]
    if average_dict[i] < min_criterion:
        min_criterion = average_dict[i]

for i in average_dict:
    if max_criterion == average_dict[i]:
        print(f'{i} has maximum average with {max_criterion} between all of the students.')
    if min_criterion == average_dict[i]:
        print(f'{i} has minimum average with {min_criterion} between all of the students.')