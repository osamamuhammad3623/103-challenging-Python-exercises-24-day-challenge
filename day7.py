# =============================================================================
# Define a class with a generator which can iterate the numbers, which are
# divisible by 7, between a given range 0 and n.
# =============================================================================

class divisible_by_7:

    def by_seven(self, n):
        for num in range(1, n + 1):
            if num % 7 == 0:
                yield num

divisible = divisible_by_7()

generator = divisible.by_seven(int(input()))
for number in generator:
    print(number)
    
# =============================================================================
# A robot moves in a plane starting from the original point (0,0). The robot
# can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of
# robot movement is shown as the following:
# 
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute
# the distance from current position after a sequence of movement and original
# point. If the distance is a float, then just print the nearest integer. 
# Example: If the following tuples are given as input to the program:
# 
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 
# 2
# =============================================================================

import math
final_x, final_y = (0,0)

while True :
    string = input()
    if not string :
        break
    
    direction = string.split()[0]
    steps = int(string.split()[1])
    
    if direction == 'UP':
        final_x += steps
    
    if direction == 'DOWN':
        final_x -= steps

    if direction == 'RIGHT':
        final_y += steps

    if direction == 'LEFT':
        final_y -= steps

distance = round ( math.sqrt( (final_x**2) + (final_y**2) ) )

print (distance)
