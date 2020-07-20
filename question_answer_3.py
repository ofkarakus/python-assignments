# QUESTION:
# Write a Python code that calculates the average of scores that students took in a 
# math class at below.
# scores = {"Mary" : 85, "Susan": 75, "Barry" : 65, "Alexis" : 88, "Jane" : 45, "Tina" 
# : 100, "Tom" : 90, "Tim": 60}

# first answer

scores = {"Mary" : 85, "Susan": 75, "Barry" : 65, "Alexis" : 88, "Jane" : 45, "Tina" : 100, "Tom" : 90, "Tim": 60}

total = 0
for i in scores.values():
    total += i

avg = total / len(scores)
print(f'average of scores : {avg}')

# second answer

average = sum(scores.values()) / len(scores)
print(f'average of scores : {average}')