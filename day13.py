# =============================================================================
# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.
# =============================================================================

class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14*self.radius*self.radius
    
cir1 = Circle(5)
print (cir1.area())

# =============================================================================
# Define a class named Rectangle which can be constructed by a length
# and width. The Rectangle class has a method which can compute the area.
# 
# =============================================================================

class Rectangle():
    def __init__(self,length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length*self.width
    
rect1 = Rectangle(10, 2)
print (rect1.area())

# =============================================================================
# Define a class named Shape and its subclass Square. The Square class has
# an init function which takes a length as argument. Both classes have a
# area function which can print the area of the shape where Shape's
# area is 0 by default.
# 
# =============================================================================

class Shape():
    def __init__(self):
        pass
    
    def area():
        return 0 
    
class Square(Shape):
    def __init__(self,length):
        Shape.__init__(self)
        self.length = length
        
    def area(self):
        return self.length*self.length
    
sqr = Square(5)
print (sqr.area())

# =============================================================================
# Please raise a RuntimeError exception.
# 
# =============================================================================
raise RuntimeError('Something wrong just happened !')
