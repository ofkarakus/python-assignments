# QUESTION:
# Write a Python code that counts how many vowels and consonants a string has that a 
# user entered.

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
vows_cons = input('Enter a word, sentence, etc. : ').lower()
vows_counter = 0
cons_counter = 0

for i in vows_cons:
    if i in vowels:
        vows_counter += 1
    elif i in consonants:
        cons_counter += 1

print(f'There are/is {vows_counter} vowel(s) and {cons_counter} consonant(s) in the input.')