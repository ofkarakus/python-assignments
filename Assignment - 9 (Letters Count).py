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

sentence = input('Enter a sentence : ')
counter = 0
result = {}

for i in sentence:
    for j in range(len(sentence)):
        if i == sentence[j]:
            counter += 1
    else:
        result.update({i : counter})
        counter = 0

print(result)