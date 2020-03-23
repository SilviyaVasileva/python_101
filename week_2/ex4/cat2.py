import sys
from cat import cat

def cat_multiple(args):
	for i in range (1,len(args)):
		cat(args[i])
		if i != len(args) - 1:
			print(" ")

def main():
	cat_multiple(sys.argv)

if __name__=="__main__":
	main()