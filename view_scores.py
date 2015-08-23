# Display the score data stored in the file

from os.path import exists
from subprocess import call

def view_scores(file_name):
	
	if exists(file_name) == False:
		print "File is either not present or deleted."
		print "Please enter a valid file name"
		return
		
	txt = open(file_name).read()
	print "\nTop scores are as follows:\n"
	print "S.No.\t\t\tName\t\t\tLife"
	print txt + "\n"
	print "Press Enter to return to main menu."
	
	raw_input()
	
	call("cls", shell=True)
	return