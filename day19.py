# =============================================================================
# Please write a program to randomly print a integer number between 7 and
#  15 inclusive.
# =============================================================================

import random
num_list = range(7,16)
print (random.choice(num_list))

# =============================================================================
# Please write a program to print the running time of execution of "1+1"
#  for 100 times.
# =============================================================================

import datetime

t1 = datetime.datetime.now()
for i in range(100):
    1+1 
t2 = datetime.datetime.now()

print (t2-t1)

# =============================================================================
# Please write a program to shuffle and print the list [3,6,7,8].
# =============================================================================

import random

num = [3,6,7,8]
random.shuffle(num)
print (num)

# =============================================================================
# Please write a program to generate all sentences where subject is in 
# ["I", "You"] and verb is in ["Play", "Love"] and the object is in
#  ["Hockey","Football"].
# =============================================================================

subjects = ['I', 'You']
verbs = ['play','love']
games = ['hockey', 'football']

# i used 3 for loops if i the lists were longer
for subject in subjects:
    for verb in verbs:
        for game in games:
            print (subject, verb, game)

# this solution is fater if the games will remain only 2 
# (using only 2 for loops)
for subject in subjects:
    for verb in verbs:
        print (subject, verb, games[0])
        print (subject, verb, games[1])
