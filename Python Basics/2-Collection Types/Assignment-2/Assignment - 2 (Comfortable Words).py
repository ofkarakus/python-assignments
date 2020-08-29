# Task : Find out if the given word is "comfortable words" in relation to 
# the ten-finger keyboard use.

# A comfortable word is a word which you can type always alternating the 
# hand you type with (assuming you 
# type using a Q-keyboard and use of the ten-fingers standard).
# The word will always be a string consisting of only letters from a to z.
# Write a program to returns True if it's a comfortable word or False otherwise.

right_hand = set('yuiophjklnm')
left_hand = set('qwertasdfgzxcvb')
word = set(input())
print(bool(word.intersection(right_hand) and word.intersection(left_hand)))