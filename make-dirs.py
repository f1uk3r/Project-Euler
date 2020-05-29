# python 3
# make-dirs.py 				-Makes folder in project euler folder
# can give argument(problem number) in command line too

import os 
import requests, bs4
import sys

def main():
	if len(sys.argv) > 1:
		n = int(sys.argv[1])
	else:
		n = int(input("Problem Number: "))
	directory_name = "Problem-" + str(n)
	if not os.path.exists(directory_name):
		os.makedirs(directory_name)

if __name__ == '__main__':
	main()