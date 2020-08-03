# =============================================================================
# Given the participants' score sheet for your University Sports Day, you
# are required to find the runner-up score. You are given scores. Store
# them in a list and find the score of the runner-up.
# 
# If the following string is given as input to the program:
# 
# 5
# 2 3 6 6 5
# Then, the output of the program should be:
# 
# 5
# =============================================================================

student_num = input()
scores = input()
scores_num = [int(score) for score in set(scores.split()) ] # set() to avoid duplicates
scores_num.sort(reverse = True)
print(scores_num[1])

# =============================================================================
# You are given a string S and width W. Your task is to wrap the string
# into a paragraph of width.
# 
# If the following string is given as input to the program:
# 
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Then, the output of the program should be:
# 
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ
# =============================================================================

import textwrap

string = input()
width = int(input())

print(textwrap.fill(string,width))

# =============================================================================
# You are given a date. Your task is to find what the day is on that date.
# 
# Input
# A single line of input containing the space separated month, day and year,
# respectively, in MM DD YYYY format.
# 08 05 2015
# 
# Output
# Output the correct day in capital letters.
# WEDNESDAY
# =============================================================================

import calendar
string = input()
year = int(string.split()[2])
month = int(string.split()[0])
day = int(string.split()[1])

day_index = calendar.weekday(year, month, day)
print (calendar.day_name[day_index])

# =============================================================================
# Given 2 sets of integers, M and N, print their symmetric difference in
# ascending order. The term symmetric difference indicates those values
# that exist in either M or N but do not exist in both.
# 
# Input
# 
# The first line of input contains an integer, M.The second line contains
# M space-separated integers.The third line contains an integer, N.The
# fourth line contains N space-separated integers.
# 
# 4
# 2 4 5 9
# 4
# 2 4 11 12
# Output
# 
# Output the symmetric difference integers in ascending order, one per line.
# 
# 5
# 9
# 11
# 12
# =============================================================================

set1 = input()
set1_num = [int(num) for num in (set1.split())]

set2 = input()
set2_num = [int(num) for num in (set2.split())]

sym_difference = []
for num in set1_num:
    if num not in set2_num :
        sym_difference.append(num)
        
for num in set2_num:
    if num not in set1_num :
        sym_difference.append(num)

for i in sym_difference:
    print (i)