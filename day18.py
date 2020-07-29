# =============================================================================
# Please write a program to output a random even number between 0 and 10
# inclusive using random module and list comprehension.
# =============================================================================

import random
print ( random.choice(range(0,11,2)) )

# =============================================================================
# Please write a program to output a random number, which is divisible by
# 5 and 7, between 10 and 150 inclusive using random module and list
# comprehension.
# =============================================================================

import random
num_list = [i for i in range(10,151) if i%35==0]
print (random.choice(num_list))

# =============================================================================
# Please write a program to generate a list with 5 random numbers between
#  100 and 200 inclusive.
# =============================================================================

import random
num_list = random.sample(range(100,201),5)
print(num_list)

# =============================================================================
# Please write a program to randomly generate a list with 5 even numbers
# between 100 and 200 inclusive.
# =============================================================================

import random
num_list = [i for i in range(100,201) if i%2==0]
generated_list = random.sample(num_list , 5)
print (generated_list)

# =============================================================================
# Please write a program to randomly generate a list with 5 numbers, which
# are divisible by 5 and 7 , between 1 and 1000 inclusive.
# =============================================================================

import random
num_list = [i for i in range(1,1001) if i%35 == 0] 
generated_list = random.sample(num_list, 5)
print (generated_list)