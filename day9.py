# =============================================================================
# Define a function which can compute the sum of two numbers.
# =============================================================================

def sum_2(num1,num2):
    return num1 + num2

print (sum_2(5,6))

# =============================================================================
# Define a function that can convert a integer into a string and print it
# in console.
# =============================================================================

def num_2_str(num):
    print (str(num))
    
num_2_str(5)

# =============================================================================
# Define a function that can receive two integer numbers in string form
# and compute their sum and then print it in console.
# =============================================================================

def sum_str(num_str1, num_str2):
    print ( int(num_str1) + int(num_str2) )
    
sum_str("5",'4') 

# =============================================================================
# Define a function that can accept two strings as input and concatenate
# them and then print it in console.
# =============================================================================

def concat(str1,str2):
    print (str1 + str2)
    
concat("My name is ", "Osama Muhammad")

# =============================================================================
# Define a function that can accept two strings as input and print the string
# with maximum length in console. If two strings have the same length,
# then the function should print all strings line by line.
# 
# =============================================================================

def long_str(str1,str2):
    if len(str1) > len(str2):
        print (str1)
    elif len(str1) == len(str2):
        print (str1)
        print (str2)
    else: #if str2 is longer
        print (str2)