import random

# this simpy return a random value and Range
# corresponding to given level
# Since python does not support 'switch' statement,
# switcher array/list is used
def calc_random_range(level):
	base = 0
	switcher = {
		1: 15,
		2: 30,
		3: 50,
		4: 100
	}
	
	# get() takes two parameters, 
	# 1. case number
	# 2. default value
	# and return the value of corresponding case
	range_val = switcher.get(level, 15)
	
	# to generate random integer between 0 and range
	rand_val = random.randint(base, range_val)
	return rand_val, range_val