# =============================================================================
# Please write a program to print the list after removing even numbers
# in [5,6,77,45,22,12,24].
# =============================================================================

numbers = [5,6,77,45,22,12,24]
odds = []
for num in numbers :
    if num%2 != 0 :
        odds.append(num)
        
print (odds)

# =============================================================================
# By using list comprehension, please write a program to print the list
#  after removing numbers which are divisible by 5 and 7 in
#  [12,24,35,70,88,120,155].
# =============================================================================

numbers = [12,24,35,70,88,120,155]
new_num = [num for num in numbers if num%5 == 0 and num%7 ==0]
print (new_num)

# =============================================================================
# By using list comprehension, please write a program to print the list
# after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
# =============================================================================

numbers = [12,24,35,70,88,120,155]
new_num = []
counter = 0 
for num in numbers:
    if counter == 0 or counter == 2 or counter == 4 or counter == 6:
        pass
    else:
        new_num.append(num)
    counter += 1
        
print (new_num)

# =============================================================================
# By using list comprehension, please write a program to print the list
# after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].
# =============================================================================

numbers = [12,24,35,70,88,120,155]
new_num = []
counter = 0 
for num in numbers:
    if counter >= 2 and counter <= 4:
        pass
    else:
        new_num.append(num)
    counter += 1
        
print (new_num)

# =============================================================================
# By using list comprehension, please write a program generate a 3*5*8 3D
# array whose each element is 0.
# =============================================================================

multi_d_array = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
                 