# Unusual places to find 'else'

# after foor loops
# The else block will run only if and when the for loop runs to completion (i.e., not if the for is aborted with a break).

from random import randint

for i in range(randint(1, 2), 6, 2):
    if i % 2 == 0:
        break  # break if even number found
else:
    # print("no even number found")
    pass


# after while loops
# The else block will run only if and when the while loop exits because the condi‐ tion became falsy (i.e., not if the while is aborted with a break).

j = randint(1, 2)
while j < 6:
    if j % 2 == 0:
        break
    j += 2
else:
    # print("nop, we did not find any evens")
    pass

# after try/except clause
# The else block will run only if no exception is raised in the try block.
# The official docs also state:
# “Exceptions in the else clause are not handled by the preced‐ ing except clauses.”

try:
    p = randint(1, 2)
    if p % 2 == 0:
        raise Exception("Even Num found!")
except:
    pass
else:
    # print("no even number found!")
    pass
