# =============================================================================
# Please write a program which count and print the numbers of each character
#  in a string input by console.
# 
# Example: If the following string is given as input to the program:
# 
# abcdefgabc
# Then, the output of the program should be:
# 
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1
# =============================================================================

string = 'abcdefgabc'
letter_dictionary = {}

for letter in string:
    letter_dictionary[letter] = letter_dictionary.get(letter, 0) +1
    
for key,value in letter_dictionary.items():
    print(key,',', value)
    
# =============================================================================
# Please write a program which accepts a string from console and print
#  it in reverse order.
# 
# Example: If the following string is given as input to the program:*
# 
# rise to vote sir
# Then, the output of the program should be:
# 
# ris etov ot esir
# =============================================================================

string = input()
print ( string[::-1])

# =============================================================================
# Please write a program which accepts a string from console and print
#  the characters that have even indexes.
# 
# Example: If the following string is given as input to the program:
# 
# H1e2l3l4o5w6o7r8l9d
# Then, the output of the program should be:
# 
# Helloworld
# =============================================================================

string = input()
print (string[::2])

# =============================================================================
# Please write a program which prints all permutations of [1,2,3]
# =============================================================================

import itertools
num = [1,2,3]
all_permutations = list(itertools.permutations(num))
print(all_permutations)

# =============================================================================
# Write a program to solve a classic ancient Chinese puzzle: We count 35
# heads and 94 legs among the chickens and rabbits in a farm. How many
# rabbits and how many chickens do we have?
#==============================================================================

heads = 35
legs = 94

for head in range(heads +1 ) :
    rabbit_heads = head
    chicken_head = heads - rabbit_heads
    all_legs = rabbit_heads*4 + chicken_head*2
    if all_legs == legs :
        print ('Chicken:', chicken_head)
        print ('Rabbit:', rabbit_heads)