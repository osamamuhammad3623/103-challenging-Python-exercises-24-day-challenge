# =============================================================================
# Assuming that we have some email addresses in the 
# "username@companyname.com" format, please write program to print the
# company name of a given email address. Both user names and company names
# are composed of letters only.
# 
# Example: If the following email address is given as input to the program:
# 
# john@google.com
# Then, the output of the program should be:
# 
# google
# =============================================================================

email = input()
after_at_symbol = email.split('@')[1]
company_name = after_at_symbol.split('.')[0]
print (company_name)

# =============================================================================
# Write a program which accepts a sequence of words separated by whitespace
# as input to print the words composed of digits only.
# 
# Example: If the following words is given as input to the program:
# 
# 2 cats and 3 dogs.
# Then, the output of the program should be:
# 
# ['2', '3']
# =============================================================================

string = input()
num_list = []
for char in string :
    try:
        num = int(char)
    except:
        continue
    else:
        num_list.append(char)

print (num_list)

# =============================================================================
# Print a unicode string "hello world".

# =============================================================================
string = u"hello world"
print (string)

# =============================================================================
# Write a program to read an ASCII string and to convert it to a unicode
# string encoded by utf-8.
# =============================================================================

string = "my name is Osama"
print (string.encode('utf-8'))

# =============================================================================
# Write a special comment to indicate a Python source code file is in unicode.
# =============================================================================

# */*/* coding : utf-8 *\*\*

# =============================================================================
# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input
# by console (n>0).
# 
# Example: If the following n is given as input to the program:
# 
# 5
# Then, the output of the program should be:
# 
# 3.55
# =============================================================================
n = int(input())
total = 0
for i in range(1, n+1):
    total += i/(i+1)
    
print( round(total, 2))