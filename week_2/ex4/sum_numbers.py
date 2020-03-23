import sys

def sum_numbers(arg):
	s = ''
	with open (arg, "r") as f:
		s = f.read()
	arr = [int(number) for number in s.split()]

	return sum(arr)

def main():
	print(sum_numbers(sys.argv[1]))


if __name__ == "__main__":
	main()