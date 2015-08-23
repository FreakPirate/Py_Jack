from submit import *

# Prints the Result and saves the data if the user has won
def conclusion(life,ans, name, file_name):
	if life == 0:
		print "\nSorry to inform you %r, but you \'Lost the Game\'.\nNice try though." %name
		print "The answer was: %d" %ans
		print "Better Luck next time!\n"
	else:
		print "\nHurray!\nYou Won %s.\nAwesome!\n" %name
		submit(name, life, file_name)