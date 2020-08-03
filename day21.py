# =============================================================================
# By using list comprehension, please write a program to print the list
#  after removing the value 24 in [12,24,35,24,88,120,155].
# =============================================================================

num = [12,24,35,24,88,120,155]
new = []
for i in num:
    if i != 24:
        new.append(i)
        
print (new)

# =============================================================================
# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
#  write a program to make a list whose elements are intersection of the
#  above given lists.
# =============================================================================

l1 = [1,3,6,78,35,55]
l2 = [12,24,35,24,88,120,155]

s1 = set(l1)
s2 = set(l2)

s1 &= s2 # means s1 = s1 & s2 (to return the intersection, that is, elements
            # that exist in both sets)
print (s1)

# =============================================================================
# With a given list [12,24,35,24,88,120,155,88,120,155], write a program
#  to print this list after removing all duplicate values with original
#  order reserved.
# =============================================================================

num = [12,24,35,24,88,120,155,88,120,155]

for i in num:
    if num.count(i) > 1:
        num.remove(i)
        
print(num)