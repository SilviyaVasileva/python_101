import unittest
from ex1 import sum_of_digits, to_digits, to_number, fact_digits, palindrome,\
count_vowels, count_consonants, char_histogram, sum_matrix, nan_expend,\
prime_factorization, group, max_consecutive

class TestSumOfDigits(unittest.TestCase):
	def test_with_one_digit_number(self):
		n = 1
		res = sum_of_digits(n)
		self.assertEqual(res, 1)
	def test_with_one_digit_number_negative(self):
		n = -1
		res = sum_of_digits(n)
		self.assertEqual(res, 1)
	def test_with_two_digits_number(self):
		n = 15
		res = sum_of_digits(n)
		self.assertEqual(res, 6)
	def test_with_even_digits_number(self):
		n = 1569
		res = sum_of_digits(n)
		self.assertEqual(res, 21)
	def test_with_odd_digits_number(self):
		n = 15694
		res = sum_of_digits(n)
		self.assertEqual(res, 25)
	def test_with_negative_number(self):
		n = -156900
		res = sum_of_digits(n)
		self.assertEqual(res, 21)

class TestToDigits(unittest.TestCase):
	def test_with_one_digit_number(self):
		n = 4
		res = to_digits(n)
		self.assertEqual(res, [4])
	def test_with_three_digits_number(self):
		n = 456
		res = to_digits(n)
		self.assertEqual(res, [4,5,6])
	def test_with_even_digits_number(self):
		n = 999999
		res = to_digits(n)
		self.assertEqual(res, [9,9,9,9,9,9])
	def test_with_odd_digits_number(self):
		n = 45678
		res = to_digits(n)
		self.assertEqual(res, [4,5,6,7,8])

class TestToNumber(unittest.TestCase):
	def test_with_one_number_arrey(self):
		arr = [9]
		res = to_number(arr)
		self.assertEqual(res, 9)
	def test_with_two_number_arrey(self):
		arr = [1,2]
		res = to_number(arr)
		self.assertEqual(res, 12)
	def test_with_odd_number_arrey(self):
		arr = [1,5,7,5,0]
		res = to_number(arr)
		self.assertEqual(res, 15750)
	def test_with_even_numberss_arrey(self):
		arr = [9,9,9,9,9,9]
		res = to_number(arr)
		self.assertEqual(res, 999999)
	def test_with_more_number_arrey(self):
		arr = [91,56,3,4,123,78,534,1]
		res = to_number(arr)
		self.assertEqual(res, 915634123785341)

class TestFactDigits(unittest.TestCase):
	def test_with_zero(self):
		n = 0
		res = fact_digits(n)
		self.assertEqual(res, 1)
	def test_with_one(self):
		n = 1
		res = fact_digits(n)
		self.assertEqual(res, 1)
	def test_with_number_with_zeros(self):
		n = 1002
		res = fact_digits(n)
		self.assertEqual(res, 5)
	def test_with_one_digit_number(self):
		n = 3
		res = fact_digits(n)
		self.assertEqual(res, 6)
	def test_with_odd_digit_number(self):
		n = 145
		res = fact_digits(n)
		self.assertEqual(res, 145)
	def test_with_even_digit_number(self):
		n = 1450
		res = fact_digits(n)
		self.assertEqual(res, 146)

class TestPalindrome(unittest.TestCase):
	def test_with_one_symbol(self):
		n = 'a'
		res = palindrome(n)
		self.assertTrue(res)
	def test_with_two_symbols_palindrome(self):
		n = 11
		res = palindrome(n)
		self.assertTrue(res)
	def test_with_two_symbols_not_palindrome(self):
		n = 'ad'
		res = palindrome(n)
		self.assertFalse(res)
	def test_with_three_symbols_palindrome(self):
		n = 'sis'
		res = palindrome(n)
		self.assertTrue(res)
	def test_with_three_symbols_not_palindrome(self):
		n = 123
		res = palindrome(n)
		self.assertFalse(res)
	def test_with_more_symbols_palindrome(self):
		n = 'siasais'
		res = palindrome(n)
		self.assertTrue(res)
	def test_with_more_symbols_not_palindrome(self):
		n = 'asdfgsa'
		res = palindrome(n)
		self.assertFalse(res)

class TestCountVowels(unittest.TestCase):
	def test_with_none_Vowels(self):
		n = 'sth'
		res = count_vowels(n)
		self.assertEqual(res, 0)
	def test_with_one_Vowel(self):
		n = 'why?'
		res = count_vowels(n)
		self.assertEqual(res, 1)
	def test_with_two_Vowels(self):
		n = 'life'
		res = count_vowels(n)
		self.assertEqual(res, 2)
	def test_with_more_Vowels(self):
		n = 'I hate covid-19'
		res = count_vowels(n)
		self.assertEqual(res, 5)

class TestCountConsonants(unittest.TestCase):
	def test_with_none_consonants(self):
		n = 'Aaaa!'
		res = count_consonants(n)
		self.assertEqual(res, 0)
	def test_with_one_consonant(self):
		n = 'Aaaah!'
		res = count_consonants(n)
		self.assertEqual(res, 1)
	def test_with_two_consonants(self):
		n = 'Haha!'
		res = count_consonants(n)
		self.assertEqual(res, 2)
	def test_with_moree_consonants(self):
		n = 'I hate covid-19!'
		res = count_consonants(n)
		self.assertEqual(res, 5)

class TestCharHistogram(unittest.TestCase):
	def test_with_one_symbol(self):
		n = 'a'
		res = char_histogram(n)
		self.assertEqual(res, {'a':1})
	def test_with_unique_symbols(self):
		n = 'Python!'
		res = char_histogram(n)
		self.assertEqual(res, { 'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1 })
	def test_with_more_symbols(self):
		n = 'AAAAaaa!!!'
		res = char_histogram(n)
		self.assertEqual(res, {'A':4, 'a': 3, '!':3})
		
class TestSumMatrix(unittest.TestCase):
	def test_one(self):
		m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		res = sum_matrix(m)
		self.assertEqual(res, 0)
	def test_two(self):
		m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
		res = sum_matrix(m)
		self.assertEqual(res, 45)
	def test_three(self):
		m =  [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
		res = sum_matrix(m)
		self.assertEqual(res, 55)
		
class TestNanExpend(unittest.TestCase):
	def test_zero(self):
		n = 0
		res = nan_expend(n)
		self.assertEqual(res, "")
	def test_one(self):
		n = 1
		res = nan_expend(n)
		self.assertEqual(res, "Not a NaN")
	def test_two(self):
		n = 2
		res = nan_expend(n)
		self.assertEqual(res, "Not a Not a NaN")
	def test_two(self):
		n = 3
		res = nan_expend(n)
		self.assertEqual(res, "Not a Not a Not a NaN")

class TestpPimeFactorization(unittest.TestCase):
	def test_with_prime_number(self):
		n = 89
		res = prime_factorization(n)
		self.assertEqual(res, [(89, 1)])
	def test_with_ten(self):
		n = 10
		res = prime_factorization(n)
		self.assertEqual(res, [(2, 1),(5,1)])
	def test_with_fourteen(self):
		n = 14
		res = prime_factorization(n)
		self.assertEqual(res, [(2, 1),(7,1)])
	def test_with_356(self):
		n = 356
		res = prime_factorization(n)
		self.assertEqual(res, [(2, 2),(89,1)])
	def test_with_1000(self):
		n = 1000
		res = prime_factorization(n)
		self.assertEqual(res, [(2, 3),(5,3)])

class TestGroup(unittest.TestCase):
	def test_with_one_element(self):
		n = [1]
		res = group(n)
		self.assertEqual(res, [[1]])
	def test_with_same_munber(self):
		n = [1,1,1]
		res = group(n)
		self.assertEqual(res, [[1,1,1]])
	def test_with_more_elements(self):
		n = [1,2,2,3,2,2,2,4,]
		res = group(n)
		self.assertEqual(res, [[1],[2,2],[3],[2,2,2],[4]])
						
class TestMaxConsecutive(unittest.TestCase):
	def test_one(self):
		n = [1,2,3]
		res = max_consecutive(n)
		self.assertEqual(res, 1)
	def test_odd(self):
		n = [1,2,2,3,3,3]
		res = max_consecutive(n)
		self.assertEqual(res, 3)
	def test_even(self):
		n = [1,2,2,2,3,3,4,4,4,4,3,3,3,2,5,2,2,3]
		res = max_consecutive(n)
		self.assertEqual(res, 4)

if __name__ == '__main__':
	unittest.main()
		