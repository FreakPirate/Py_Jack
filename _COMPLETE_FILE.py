"""
	Old Jackpot Game in 'Python'
"""
import random
from subprocess import call
from os.path import exists
#import sys

def instructions(arg):
	inst_str = """
	\t\t\t** Jackpot **
	Hii, %s
	Goal: Guess the number which the computer selected randomly.
	Chances/Lives: 5
	Hint: [Big, Small, Too Big, Too small] compared to that number.\n
	"""
	call("cls", shell=True)
	print inst_str % arg
	

def level_select():
	lvl_str = """
	Select a level based on the range:\n
	1. Rookie (Range: 0-15)
	2. Mediocre (Range: 0-30)
	3. Not-So-Easy (Range: 0-50)
	4. Insane (Range: 0-100)\n
	Choose Wisely.
	"""
	
	while True:
		print lvl_str
		lvl = int(raw_input('> '))
		
		if all(lvl != x for x in (1,2,3,4)):
			print "Bad Choice!"
			print "Select Again."
		else:
			return lvl
	
def calc_random_range(level):
	base = 0
	switcher = {
		1: 15,
		2: 30,
		3: 50,
		4: 100
	}
	range_val = switcher.get(level, 15)
	rand_val = random.randint(base, range_val)
	return rand_val, range_val
	
		
def game_logic(rand_num, range_val, life):
	hint_1 = "Small but Close."
	hint_2 = "Large but Close."
	hint_3 = "Too Small"
	hint_4 = "Too Large"
	
	hint_range = int(range_val / 3)
	print "log:%d"%hint_range
	while life >= 1:
		print "Guess the number:"
		guess = int(raw_input('> '))
		
		life = life - 1
		
		if (guess>range_val) or (guess < 0):
			print "Enter the number within the range: %d - %d" %(0, range_val)
			continue
		
		if guess == rand_num:
			return life
			
		elif guess > rand_num:
			if (guess - rand_num) <= hint_range:
				print hint_2
			else:
				print hint_4
				
		elif guess < rand_num:
			if (rand_num - guess) <= hint_range:
				print hint_1
			else:
				print hint_3
				
		print "Remaining Life: %d" %life
	
	return life
		
			
	
def conclusion(life,ans, name, file_name):
	if life == 0:
		print "\nSorry to inform you %s, but you \'Lost the Game\'.\nNice try though." %name
		print "The answer was: %d" %ans
		print "Better Luck next time!\n"
	else:
		print "\nHurray!\nYou Won %s.\nAwesome!\n" %name
		submit(name, life, file_name)
	
def submit(name, life, file_name):
	# File entry
	if exists(file_name)==False or len(open(file_name).read())<5:
		print "File not present!\nMaking a new file."
		fil_w = open(file_name, 'w')
		fil_w.write('1' + "\t\t" + name + "\t\t\t" + str(life))
		fil_w.close()		
	else:	
		fil_read = open(file_name, 'r')
		fil_ap = open(file_name, 'a')
		
		data = fil_read.read()
		count = int( data.split('\n').pop(-1).split('\t\t').pop(0)) 
		print count
		++count
		fil_read.close()
		
		tabs1 = "\t\t"
		tabs2 = "\t\t\t"
		write_data = "\n" + str(count) + tabs1 + name + tabs2 + str(life)
		fil_ap.write(write_data)
		fil_ap.close()
		
	print "Scores entered successfully..."
		


# Program starts here
life = 5
file_name_perm = "top_score.txt"

print "Enter your credentials:"
name = raw_input("Name> ")

while True:
	instructions(name)
	
	level = level_select()
	rand_val, range_val = calc_random_range(level)
	
	life_left = game_logic(rand_val, range_val, life)
	
	conclusion(life_left, rand_val, name, file_name_perm)
	
	print "Type \'quit()\' to exit."
	print "or Press Enter to continue..."
	
	desc = raw_input('> ')
	
	if desc == "":
		# flush the variables
		level = 0
		result = ''
	else:
		break
	

print "Thank's for staying!\nBye."		