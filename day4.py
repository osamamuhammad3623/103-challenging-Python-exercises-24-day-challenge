# =============================================================================
# Write a program that accepts a sentence and calculate the number of upper
# case letters and lower case letters.
# 
# Suppose the following input is supplied to the program:
# 
# Hello world!
# Then, the output should be:
# 
# UPPER CASE 1
# LOWER CASE 9
# =============================================================================

sentense = input()
lower = 0
upper = 0
for letter in sentense:
    if letter.isspace(): continue
    #checking if the character is upper and an alphapetical letter !
    if letter == letter.upper() and letter.isalpha():
        upper += 1
    if letter == letter.lower() and letter.isalpha():
        lower += 1
print ("UPPER CASE", upper)
print("LOWER CASE", lower)

# =============================================================================
# Write a program that computes the value of a+aa+aaa+aaaa with a given
# digit as the value of a.
# 
# Suppose the following input is supplied to the program:
# 
# 9
# Then, the output should be:
# 
# 11106
# =============================================================================

a_value = input()
total = 0
temp = ""

for i in range(4):
    temp += a_value               # concatenating 'a' to 'tmp'
    total += int(temp)      # converting string type to integer type

print(total)