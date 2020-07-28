# =============================================================================
# Please write assert statements to verify that every number in the
# list [2,4,6,8] is even.
# =============================================================================

the_list = [2,4,6,8]
for i in the_list :
    assert i%2 == 0, (str(i) + ' is not an even number')
    
# =============================================================================
# Please write a program which accepts basic mathematic expression
# from console and print the evaluation result.
# 
# Example: If the following n is given as input to the program:
# 
# 35 + 3
# Then, the output of the program should be:
# 
# 38
# =============================================================================

math_string = input()
print(eval(math_string))

# =============================================================================
# Please write a binary search function which searches an item in a
# sorted list. The function should return the index of element to be
# searched in the list.
# 
# =============================================================================

def bi_search(num_list , left_index, right_index, number):
    mid = int((left_index + right_index) / 2)
    if num_list[mid] == number :
        return mid
    elif num_list[mid] > number:
        return bi_search(num_list, 0, mid, number)
    elif num_list[mid] < number :
        return bi_search(num_list, mid, right_index, number)

my_list = [1,3,5,7,9,12,16]
print (bi_search(my_list, 0, len(my_list) -1 , 7))

# =============================================================================
# Please generate a random float where the value is between 10 and 100
# using Python module.
# =============================================================================

import random
num = random.uniform(10, 100)
print (num)

# =============================================================================
# Please generate a random float where the value is between 5 and 95
# using Python module.
# 
# =============================================================================

import random
num = random.uniform(5, 95)
print (num)
