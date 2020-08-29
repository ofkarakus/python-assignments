# Given a non-empty string and an int n, return a new string where the character at 
# index n has been removed. The value of n will be a valid index of a character in 
# the original string (i.e. n will be in the range 0....len(str)-1 inclusive).

def missing_char(word, n):
    new_word = ''
    for i in word:
        if word.index(i) != n:
            new_word += i
    return new_word

print(missing_char('kitchen', 1))
print(missing_char('kitchen', 0))
print(missing_char('kitchen', 4))