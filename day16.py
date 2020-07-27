# =============================================================================
# Write a program to compute:
# 
# f(n)=f(n-1)+100 when n>0
# and f(0)=0
# with a given n input by console (n>0).
# 
# Example: If the following n is given as input to the program:
# 
# 5
# Then, the output of the program should be:
# 
# 500
# =============================================================================

def calculate_n(n):
    
    result = 0
    while (n > 0):
        result += 100 
        n -= 1
    return result

print(calculate_n(int(input())))

# =============================================================================
# The Fibonacci Sequence is computed based on the following formula:
# 
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input
#  by console.
# 
# Example: If the following n is given as input to the program:
# 
# 7
# Then, the output of the program should be:
# 
# 13
# =============================================================================

def fab(n):
    
    if n == 0 : return 0
    if n == 1 : return 1
    return fab(n-1) + fab(n-2)
        
print(fab(int(input())))

# =============================================================================
# The Fibonacci Sequence is computed based on the following formula:
# 
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n
#  input by console.
# 
# Example: If the following n is given as input to the program:
# 
# 7
# Then, the output of the program should be:
# 
# 0,1,1,2,3,5,8,13
# =============================================================================

def fab(n):
    
    print (n)
    if n == 0 : return 0
    if n == 1 : return 1
    return fab(n-1) + fab(n-2)
        
print(fab(int(input())))

# =============================================================================
# Please write a program using generator to print the even numbers
# between 0 and n in comma separated form while n is input by console.
# 
# Example: If the following n is given as input to the program:
# 
# 10
# Then, the output of the program should be:
# 
# 0,2,4,6,8,10
# =============================================================================

n = int(input())

for i in range(0, n+1, 2):
  if i < n - 1:
    print(i, end = ',' )
  else:
    print(i)
    
# =============================================================================
# Please write a program using generator to print the numbers which
# can be divisible by 5 and 7 between 0 and n in comma separated
# form while n is input by console.
# 
# Example: If the following n is given as input to the program:
# 
# 100
# Then, the output of the program should be:
# 
# 0,35,70
# 
# =============================================================================

def generate(n):
    for i in range(n+1):
        if i % 35 == 0:
            yield i

n = int(input())
num_list = [int(i) for i in generate(n)]
print(num_list)