"""
	Old Jackpot Game in 'Python'
	New Added Features:
		1. Support for saving top scores
		2. Faster and more interactive
		3. Increased maturity
	
	TODO:
		Save file in sorted order of scores rather randomly.
"""

# importing all the required functions and Features
# each module feature is explained in respective module

from conclusion import *
from game_logic import *
from instructions import *
from level_select import *
		

# Life is the number of wrong choices allowed
life = 5
# Score are stored in the file below
file_name_perm = "top_score.txt"


print "Enter your credentials:"
user_name = raw_input("Name> ")

while True:
	# Random Value and Range for the particular level
	rand_val, range_val = level_select(file_name_perm, user_name)
	
	# saving remaining life
	life_remain = game_logic(rand_val, range_val, life)
	
	# Printing result or conclusion
	conclusion(life_remain, rand_val, user_name, file_name_perm)
	
	print "Type \'quit()\' to exit."
	print "or Press Enter to continue..."
	
	desc = raw_input('> ')
	
	# Check for exit or continue
	# "" this means Enter key was pressed
	if desc == "":
		# flush the variables
		level = 0
		result = ''
	else:
		break
	

print "Thank's for staying!\nBye."		