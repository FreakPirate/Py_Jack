from subprocess import call

# simple instructions
def instructions(arg):
	inst_str = """
	\t\t\t** Jackpot **
	Hii, %s
	Goal: Guess the number which the computer selected randomly.
	Chances/Lives: 5
	Hint: [Big, Small, Too Big, Too small] compared to that number.\n
	"""
	
	# call() is used to run the shell commands inside python
	call("cls", shell=True)
	print inst_str % arg