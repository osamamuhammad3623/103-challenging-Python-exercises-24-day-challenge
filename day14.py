# =============================================================================
# Write a function to compute 5/0 and use try/except to catch the exceptions.
# =============================================================================

def divide_by_zero():
    return (5/0)
try :
    divide_by_zero()
except:
    print ('Division By Zero !')
    
# =============================================================================
# Define a custom exception class which takes a string message as attribute.
# =============================================================================

class my_exception():
    
    def __init__(self, message):
        self.message = message
        
try:
    number = int(input())
except:
    exception = my_exception('Not a number!')
    print(exception.message)
    
# =============================================================================
# Assuming that we have some email addresses in the
# "username@companyname.com" format, please write program to print the
# user name of a given email address. Both user names and company names
# are composed of letters only.
# 
# Example: If the following email address is given as input to the program:
# 
# john@google.com
# Then, the output of the program should be:
# 
# john
# 
# In case of input data being supplied to the question, it should be assumed
# to be a console input.
# 
# =============================================================================

email = input()
split = email.split('@')
print (split[0])
