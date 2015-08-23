def game_logic(rand_num, range_val, life):
	hint_1 = "Small but Close."
	hint_2 = "Large but Close."
	hint_3 = "Too Small"
	hint_4 = "Too Large"
	
	hint_range = int(range_val / 3)
	
	# print "log:%d"%hint_range
	
	while life >= 1:
		print "Guess the number:"
		guess = int(raw_input('> '))
		
		life = life - 1
		
		# out of range boundaries check
		if (guess>range_val) or (guess < 0):
			print "Enter the number within the range: %d - %d" %(0, range_val)
			continue
		
		# win check
		if guess == rand_num:
			return life
		
		# Large number entered	
		elif guess > rand_num:
			if (guess - rand_num) <= hint_range:
				print hint_2
			else:
				print hint_4
		
		# Small number entered		
		elif guess < rand_num:
			if (rand_num - guess) <= hint_range:
				print hint_1
			else:
				print hint_3
				
		print "Remaining Life: %d" %life
	
	return life