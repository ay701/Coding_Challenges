# Given a function which produces a random integer in the range 1 to 5, 
# write a function which produces a random integer in the range 1 to 7.

import random

def random15():
	return random.randint(1,5)

def random15_17():

    while True:
        num = 5 * random15() + random15() - 5
        if num<=21:
            break
    
    return num%7 + 1

print random15_17()