# =============================================================================
# Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.
# suppose the following input is supplied to the program:
# 
# 34,67,55,33,12,98
# Then, the output should be:
# 
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# =============================================================================

list_string = input()

the_list = list_string.split(',')
the_tuple = tuple(the_list)
print (the_list)
print (the_tuple)

# =============================================================================
# Define a class which has at least two methods:
# 
# getString: to get a string from console input
# printString: to print the string in upper case.
# =============================================================================

class string_class():        
            
    def get_string(self):
        self.string = input()
    
    def print_string(self):
        print(self.string.upper())
        
my_string = string_class()
my_string.get_string()
my_string.print_string()

# =============================================================================
# Write a program that calculates and prints the value according to the given
# formula:
# 
# Q = Square root of [(2 _ C _ D)/H]
# 
# Following are the fixed values of C and H:
# 
# C is 50. H is 30.
# 
# D is the variable whose values should be input to your program in a
# comma-separated sequence.For example Let us assume the following comma
# separated input sequence is given to the program:
# 
# 100,150,180
# The output of the program should be:
# 
# 18,22,24
# =============================================================================

import math
c = 50 
h = 30 
d_list = input()
answer_string = ""
d_numbers = d_list.split(',')

for num in d_numbers:
    d_value = int(num)
    q = math.sqrt( (2*c*d_value) / h )
    answer_string += str(int(q)) + ","

#printing answer_string except for the last character because it'll be a comma
print(answer_string[:-1]) 

# =============================================================================
# Write a program which takes 2 digits, X,Y as input and generates a
# 2-dimensional array. The element value in the i-th row and j-th column
# of the array should be i*j.
# 
# =============================================================================

x_y = input()
x = int(x_y.split(',')[0])
y= int(x_y.split(',')[1])

matrix = [[i*j for j in range(y)] for i in range(x)]

print (matrix)

# =============================================================================
# Write a program that accepts a comma separated sequence of words as
# input and prints the words in a comma-separated sequence after sorting
# them alphabetically.
# 
# Suppose the following input is supplied to the program:
# 
# without,hello,bag,world
# Then, the output should be:
# 
# bag,hello,without,world
# 
# =============================================================================

sentense = input()
word_list = sentense.split(',')

print(sorted(word_list))

# =============================================================================
# Write a program that accepts sequence of lines as input and prints the
# lines after making all characters in the sentence capitalized.
# 
# Suppose the following input is supplied to the program:
# 
# Hello world
# Practice makes perfect
# Then, the output should be:
# 
# HELLO WORLD
# PRACTICE MAKES PERFECT
# 
# =============================================================================

lines = []
while True :
    new_line = input()
    if new_line:  #if the user enter a new line, it's added to the list
        lines.append(new_line.upper())
    else:         #if the user pressed Enter without entering a new line
        break

for each in lines:
    print(each)