"""
Practical 4 warmup question with lists
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

## commands and answers ##

numbers[0]
# the number 3
numbers[-1]
# the number 2
numbers[3]
# the number 1
numbers[:-1]
# [3, 1, 4, 1, 5, 9]
numbers[3:4]
######################## [1]
5 in numbers
# True
7 in numbers
# False
"3" in numbers
# False
numbers + [6, 5, 3]
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


## Python expressions ##

# 1

numbers[0] = 10

# 2

numbers[-1] = 1

# 3

numbers[2:]

# 4

9 in numbers
