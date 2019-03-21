

import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Some Outputs:
#
# 20
# 9
# 2.9409281500858704
#
# 8
# 9
# 2.9815585128809508
#
# 10
# 3
# 3.5247750977436496

# smallest number on line 1 is 5 and largest is 20
# smallest number on line 2 is 3 and largest is 10 and no it cannot produce 4 since in steps of 2 from 3
# smallest number on line 3 is 2.5 and largest is 5.5