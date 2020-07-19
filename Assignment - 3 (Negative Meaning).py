# Task

# Define a function to take a word and return negative meaning.
# Given a word, return a new word where "not " has been added to the front. However, if the word already 
# begins with "not", return the string unchanged.

def not_string(word):
    if word[0:3] == 'not':
        return word
    else:
        return 'not {}'.format(word)


# Tests

print(not_string('sugar'))
print(not_string('x'))
print(not_string('not bad'))