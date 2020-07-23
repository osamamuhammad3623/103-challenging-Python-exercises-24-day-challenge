# =============================================================================
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the
# first half values in one line and the last half values in one line.
# =============================================================================

num_tuple = (1,2,3,4,5,6,7,8,9,10)
print (num_tuple[:5])
print (num_tuple[5:])

# =============================================================================
# Write a program to generate and print another tuple whose values are
# even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
# =============================================================================

num_tuple = (1,2,3,4,5,6,7,8,9,10)
even_tuple = tuple(i for i in num_tuple if i %2 == 0)
print (even_tuple)

# =============================================================================
# Write a program which accepts a string as input to print "Yes" if the
# string is "yes" or "YES" or "Yes", otherwise print "No".
# =============================================================================

string = input()
if string == 'YES' or string == 'yes' or string =='Yes': print ("Yes")
else: print ("No")

# =============================================================================
# Write a program which can map() to make a list whose elements are square
# of elements in [1,2,3,4,5,6,7,8,9,10].
# =============================================================================

num_list = [1,2,3,4,5,6,7,8,9,10]
sqr_num =map(lambda i:i**2,num_list )
print(list(sqr_num))

# =============================================================================
# Write a program which can map() and filter() to make a list whose
# elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
# 
# =============================================================================

num_list = [1,2,3,4,5,6,7,8,9,10]
even_num = filter(lambda num: num%2==0, num_list)
sqr_even = map(lambda num: num**2 , even_num)
print (list(sqr_even))

# =============================================================================
# Write a program which can filter() to make a list whose elements are even
# number between 1 and 20 (both included).
# 
# =============================================================================

import numpy as np
num = np.array(np.arange(1,21))
even_num = filter(lambda i: i %2==0, num)
print (list(even_num))
