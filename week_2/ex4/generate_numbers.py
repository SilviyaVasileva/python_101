import sys
from random import randint


def generate_numbers(filename, numbers):
    #arr = []
    s = ''
    for i in range(int(numbers)):
        s += str(randint(1, 1000)) + ' '

    with open (filename, "w") as f:
        f.write(s)


def main():
    generate_numbers(sys.argv[1], int(sys.argv[2]))

if __name__ == '__main__':
    main()