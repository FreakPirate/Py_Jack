# Prints level select string and asks for a choice

from calc_random_range import *
from view_scores import *
from instructions import *

def level_select(file_name, user_name):
		
	lvl_str = """
	Select a level based on the range:\n
	1. Rookie (Range: 0-15)
	2. Mediocre (Range: 0-30)
	3. Not-So-Easy (Range: 0-50)
	4. Insane (Range: 0-100)
	
	5. View high scores
	0. Exit
	Choose Wisely.
	"""
	
	while True:
		instructions(user_name)
		print lvl_str
		lvl = int(raw_input('> '))
		
		if lvl == 0:
			print "Thanks for playing..."
			exit()
		
		elif lvl == 5:
			view_scores(file_name)
			
		elif all(lvl != x for x in (1,2,3,4)):
			print "Bad Choice!"
			print "Press Enter and Select Again."
			raw_input()
		
		else:
			return calc_random_range(lvl)