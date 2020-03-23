#
#Zadacha 1
#

def anagrams():
	is_anagram = 'NOT ANAGRAM'
	words = input('Write the words: ')
	separete = words.find(' ')
	first_word = words[:separete].lower()
	second_word = words[separete+1:].lower()

	if (len(second_word) != len(first_word)):
		return is_anagram
	else:
		if (sorted(first_word) != sorted(second_word)):
			return is_anagram
	return 'ANAGRAM'

#
#Zadacha 2
#

def is_credit_card_valid(number):
	new_number = str(number)
	if(len(new_number)%2 != 0):
		sum_numbers = 0
		for i in range(0,len(new_number), 2):
			sum_numbers += int(new_number[i])
		for i in range(1,len(new_number)-1,2):
			if (int(new_number[i])*2 > 9):
				temp_number = int(new_number[i])*2
				sum_numbers += int(str(temp_number)[0]) + int(str(temp_number)[1])
			else:
				sum_numbers += int(new_number[i])*2
		if (sum_numbers % 10 == 0):
			return '%d is a valid number' %number
	return '%d is invalid number' %number

#
#Zadacha 3
#

def is_prime(n): 
    if (n <= 1): 
        return False
    if (n <= 3): 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    x = 5
    while(x * x <= n) : 
        if (n % x == 0 or n % (x + 2) == 0) : 
            return False
        x = x + 6
    return True

def get_prime_numbers(n):
	prime_numbers = []
	for i in range(n):
		if (is_prime(i)):
			prime_numbers.append(i)
	return prime_numbers

def goldbach(n):
	prime_numbers = get_prime_numbers(n)
	first_number = 0;
	second_number = len(prime_numbers) - 1;
	res = []

	for i in range(len(prime_numbers)):
		for j in range(len(prime_numbers)-1, i-1,-1):
			if(prime_numbers[i] + prime_numbers[j]) == n:
				res.append((prime_numbers[i],prime_numbers[j]))
	return res

#
#Zadacha 4
#

def find_bigger(n1,n2):
	if (n1 > n2):
		return True
	return False

def matrix_bombing_plan(m):
	res = {}
	height = len(m)
	width = len(m[0])
	result = {}
	tempRes = {}

	for i in range(height):
		for j in range(width):
			res[(i,j)] = m[i][j]
			result[(i,j)] = m[i][j]

	for number in iter(res.keys()):
		row = number[0]
		col = number[1]

		tempRes = result.copy()

		if (row - 1 >= 0):
			if(tempRes[row - 1, col] <= tempRes[row, col]):
				tempRes[row - 1, col] = 0
			else:
				tempRes[row - 1, col] -= tempRes[row, col]
		if (row + 1 < height):
			if(tempRes[row + 1, col] <= tempRes[row, col]):
				tempRes[row + 1, col] = 0
			else:
				tempRes[row + 1, col] -= tempRes[row, col]
		if (col - 1 >= 0):
			if(tempRes[row, col - 1] <= tempRes[row, col]):
				tempRes[row, col - 1] = 0
			else:
				tempRes[row, col - 1] -= tempRes[row, col]
		if (col + 1 < width):
			if(tempRes[row, col + 1] <= tempRes[row, col]):
				tempRes[row, col + 1] = 0
			else:
				tempRes[row, col + 1] -= tempRes[row, col]
		if (row - 1 >= 0 and col - 1 >= 0):
			if(tempRes[row - 1, col - 1] <= tempRes[row, col]):
				tempRes[row - 1, col - 1] = 0
			else:
				tempRes[row - 1, col - 1] -= tempRes[row, col]
		if (row + 1 < height and col - 1 >= 0):
			if(tempRes[row + 1, col - 1] <= tempRes[row, col]):
				tempRes[row + 1, col - 1] = 0
			else:
				tempRes[row + 1, col - 1] -= tempRes[row, col]
		if (row - 1 >= 0 and col + 1 < width):
			if(tempRes[row - 1, col + 1] <= tempRes[row, col]):
				tempRes[row - 1, col + 1] = 0
			else:
				tempRes[row - 1, col + 1] -= tempRes[row, col]
		if (row + 1 < height and col + 1 < width):
			if(tempRes[row + 1, col + 1] <= tempRes[row, col]):
				tempRes[row + 1, col + 1] = 0
			else:
				tempRes[row + 1, col + 1] -= tempRes[row, col]

		res[row, col] = sum(tempRes.values())
	return res