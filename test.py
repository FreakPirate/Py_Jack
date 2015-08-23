from os.path import exists
from sys import argv

script, fil_name = argv

a = open(fil_name, 'r')
b = a.read()

c = b.split('\n')[-1].split('\t\t\t')[0]

print c
a.close()