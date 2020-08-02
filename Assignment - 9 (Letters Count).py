# Task:

# Count the number of each letter in a sentence.
# The department you work for undertook a project construction that makes word / 
# text analysis. You are asked to calculate the number of letters or any chars in 
# the sentences entered under this project.
# Write a Python program that;
# takes a sentence from the user,
# counts the number of each letter of the sentence,
# collects the letters/chars as a key and the counted numbers as a value in a 
# dictionary.

sentence_1 = input('Enter a sentence : ')
counter = 0
result_1 = {}

for i in sentence_1:
    for j in range(len(sentence_1)):
        if i == sentence_1[j]:
            counter += 1
    else:
        result_1[i] = counter  # second way to update dict.
        counter = 0

print(result_1)

# second answer

sentence_2 = input('Enter a sentence : ')
result_2 = []

for i in sentence_2:
    result_2.append([i , sentence_2.count(i)])
print(dict(result_2))

# third answer

sentence_3 = input('Enter a sentence : ')
result_3 = {}

for i in sentence_3:
    if i in result_3.keys():
        result_3[i] += 1
    else: result_3[i] = 1
print(result_3)