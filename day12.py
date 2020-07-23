# =============================================================================
# Write a program which can map() to make a list whose elements are square
# of numbers between 1 and 20 (both included).
# =============================================================================

import numpy as np
num_list = np.array(np.arange(1,21))
sqr_list = list(map(lambda i:i**2, num_list))
print (sqr_list)

# =============================================================================
# Define a class named American which has a static method called
# printNationality.
# =============================================================================

class American():
    
    @staticmethod
    def printNationality():
        print("I am American")

american = American()
american.printNationality()

# =============================================================================
# Define a class named American and its subclass NewYorker.
# =============================================================================

class American():
    pass

class new_yorker(American):
    pass

american = American()
new_yorker = new_yorker()