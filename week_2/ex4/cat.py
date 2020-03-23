import sys

def cat(arg):
	with open (arg, "r") as f:
		print(f.read())

def main():
	arg = sys.argv[1]
	cat(arg)

if __name__=="__main__":
	main()