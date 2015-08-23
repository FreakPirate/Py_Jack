from os.path import exists

def submit(name, life, file_name):
	# File entry
	
	# check if file exists or not
	# if not make new file
	if exists(file_name)==False or len(open(file_name).read())<5:
		print "File not present!\nMaking a new file."
		fil_w = open(file_name, 'w')
		fil_w.write('1' + "\t\t\t" + name + "\t\t\t" + str(life))
		fil_w.close()		
	else:
		
		# if file already exists, then fetch the S.No. value
		# increase it for next counter
		# finally append the data in specified format
		# Sno + "\t\t" + name + "\t\t\t" + life_remain
		fil_read = open(file_name, 'r')
		fil_ap = open(file_name, 'a')
		
		data = fil_read.read()
		
		# fetching the counter value or last serial number
		count = int( data.split('\n')[-1].split('\t\t\t')[0])
		# print "log:%d" %count
		
		count = count + 1
		fil_read.close()
		
		tabs = "\t\t\t"
		write_data = "\n" + str(count) + tabs + name + tabs + str(life)
		fil_ap.write(write_data)
		fil_ap.close()
		
	print "Scores entered successfully..."