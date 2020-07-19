# =============================================================================
# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# 
# Suppose the following input is supplied to the program:
# 
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or
# Python 3.
# 
# Then, the output should be:
# 
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
# =============================================================================

string = input()
string_list = string.split()
string_dictionary = {}
for word in string_list:
    if word in string_dictionary:
        string_dictionary[word] += 1
    else:
        string_dictionary[word] = 1

for key,freq in sorted(string_dictionary.items()) :
    print(key, ':', freq)  

# =============================================================================
# Write a method which can calculate square value of number
# =============================================================================

def sqr_for_num(number):
    return number**2

print (sqr_for_num(5))

# =============================================================================
# Python has many built-in functions, and if you do not know how to use it,
# you can read document online or find some books. But Python has a
# built-in document function for every built-in functions.
# 
# Please write a program to print some Python built-in functions documents,
# such as abs(), int(), raw_input()
# 
# And add document for your own function
# =============================================================================

# usign method_name.__doc__
print (abs.__doc__)
print (int.__doc__)
print (input.__doc__)

def say_my_name():
    '''Printing my name, which is Osama Muhammad'''
    return "Osama Muhammad"

print (say_my_name.__doc__)

# =============================================================================
# Define a class, which have a class parameter and have a same instance
# parameter.
# =============================================================================

class car:
    
    model = 'BMW'
    
    def __init__(self,model = None):
        self.model = model
        
new_car = car()
new_car.model = "Mercedes"
print("class parameter is", car.model, ", but the new_car model is"
      ,new_car.model)

another_car = car("Volvo")
print("class parameter is", car.model, ", but the another_car model is"
      ,another_car.model)
