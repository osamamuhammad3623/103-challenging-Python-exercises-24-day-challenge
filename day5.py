# =============================================================================
# Use a list comprehension to square each odd number in a list. The list is
# input by a sequence of comma-separated numbers. >Suppose the following input
# is supplied to the program:
# 
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 
# 1,9,25,49,81
# =============================================================================

num = input()
num_list = num.split(',')
output = [ str(int(each)**2) for each in num_list if int(each) % 2 != 0]
print (output)

# =============================================================================
# Write a program that computes the net amount of a bank account based a
# transaction log from console input. The transaction log format is shown
# as following:
# 
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# 
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 
# 500
# =============================================================================

total = 0 
while True :
    process = input()
    if not process: break
    else:
        process_part = process.split()
        if process_part[0] == 'D' :
            total += int(process_part[1])
        
        if process_part[0] == 'W' :
            total -= int(process_part[1])
print (total)