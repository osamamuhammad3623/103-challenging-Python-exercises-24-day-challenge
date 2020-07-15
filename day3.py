# =============================================================================
# Write a program that accepts a sequence of whitespace separated words as
# input and prints the words after removing all duplicate words and sorting
# them alphanumerically.
# 
# Suppose the following input is supplied to the program:
# 
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# 
# again and hello makes perfect practice world
# =============================================================================

string = input()
string_list = string.split()
string_set = set(string_list)
output = ""
for word in sorted(string_set):
    output += word + " "

print (output)

# =============================================================================
# Write a program which accepts a sequence of comma separated 4 digit binary
# numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated
# sequence.
# 
# Example:
# 
# 0100,0011,1010,1001
# Then the output should be:
# 
# 1010
# =============================================================================

numbers = input()
num_list = numbers.split(',')
for each in num_list:
    if int(each,2) %5 == 0:
        print (each)
        
# =============================================================================
# Write a program, which will find all such numbers between 1000 and 3000
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a
# single line.  
#         
# =============================================================================

num_list = range(1000, 3001)
output = ''
for num in num_list:
    num_str = str(num)
    # not to loop in numbers from 1000:1999 because '1' is not even :
    if num_str[0] == '2' :
        if num%2 == 0 and int((num/10)) %2 == 0 and int((num/100)) %2 == 0:
            output += num_str + ',' 
print (output[:-1])

# =============================================================================
# Write a program that accepts a sentence and calculate the number of letters
# and digits.
# 
# Suppose the following input is supplied to the program:
# 
# hello world! 123
# Then, the output should be:
# 
# LETTERS 10
# DIGITS 3
# =============================================================================

string = input()
numbers = 0
letters = 0
for char in string:
    if char.isspace(): continue

    if char.isdigit(): # or char.isnumeric()  
        numbers += 1 
    if char.isalpha():
        letters += 1 
print ("LETTERS", letters)
print ("DIGITS", numbers)
