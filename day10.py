# =============================================================================
# Define a function which can print a dictionary where the keys are numbers
# between 1 and 20 (both included) and the values are square of keys.
# =============================================================================

num_dictionary = {i:i**2 for i in range(1,21)}
print (num_dictionary)

# =============================================================================
# Define a function which can generate a dictionary where the keys are
# numbers between 1 and 20 (both included) and the values are square of keys.
# The function should just print the keys only.
# =============================================================================

def generate_dictionary():
    num_dictionary = {i:i**2 for i in range(1,21)}
    for key in num_dictionary.keys():
        print (key)
        
generate_dictionary()

# =============================================================================
# Define a function which can generate and print a list where the values are
# square of numbers between 1 and 20 (both included).
# =============================================================================

def generate_list():
    num_list = [i**2 for i in range(1,21)]
    print(num_list)
    
generate_list()

# =============================================================================
# Define a function which can generate a list where the values are square of
# numbers between 1 and 20 (both included). Then the function needs to
# print the first 5 elements in the list.
# =============================================================================

def generate_list():
    num_list = [i**2 for i in range(1,21)]
    print(num_list[:5])
    
generate_list()

# =============================================================================
# Define a function which can generate a list where the values are square
# of numbers between 1 and 20 (both included). Then the function needs
# to print the last 5 elements in the list.
# =============================================================================

def generate_list():
    num_list = [i**2 for i in range(1,21)]
    print(num_list[-5:])
    
generate_list()

# =============================================================================
# Define a function which can generate a list where the values are square
# of numbers between 1 and 20 (both included). Then the function needs
# to print all values except the first 5 elements in the list.
# =============================================================================

def generate_list():
    num_list = [i**2 for i in range(1,21)]
    print(num_list[5:])
    
generate_list()

# =============================================================================
# Define a function which can generate and print a tuple where the value
# are square of numbers between 1 and 20 (both included).
# =============================================================================

def generate_list():
    num_list = [i**2 for i in range(1,21)]
    print(tuple(num_list))
    
generate_list()