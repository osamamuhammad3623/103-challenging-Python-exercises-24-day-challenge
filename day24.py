# =============================================================================
# You are given a string.Your task is to count the frequency of letters of
# the string and print the letters in descending order of frequency.
# 
# If the following string is given as input to the program:
# 
# aabbbccde
# Then, the output of the program should be:
# 
# b 3
# a 2
# c 2
# d 1
# e 1
# =============================================================================

string = input()
letter_dictionary = {}

for letter in string:
    letter_dictionary[letter] = letter_dictionary.get(letter, 0) +1
    
for key,value in letter_dictionary.items():
    print(key, value)
    
# =============================================================================
# Write a Python program that accepts a string and calculate the number of
# digits and letters.
# 
# Input
# 
# Hello321Bye360
# Output
# 
# Digit - 6
# Letter - 8
# =============================================================================

string = input()
d = 0
l = 0
for i in string :
    if i.isdigit() :
        d += 1
    if i.isalpha() :
        l += 1
        
print ('Digit -', d)
print ('Letter -', l)

# =============================================================================
# Given a number N.Find Sum of 1 to N Using Recursion
# 
# Input
# 
# 5
# Output
# 
# 15
# =============================================================================

def recursive_sum(n):
    rec_sum = 0
    for i in range(1,n+1):
        rec_sum += i
    return rec_sum

print (recursive_sum(int(input())))