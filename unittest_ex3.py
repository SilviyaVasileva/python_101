from unittest.mock import patch
import unittest

from ex3 import anagrams, is_credit_card_valid, goldbach, matrix_bombing_plan

class TestAnagrams(unittest.TestCase):
	def test_one(self):
		user_input = "TOP_CODER COTO_PRODE"
		with patch('builtins.input', return_value = user_input):
			self.assertEqual(anagrams(), 'NOT ANAGRAM')
	def test_two(self):
		user_input = 'kilata cvetelina_yaneva'
		with patch('builtins.input', return_value = user_input):
			self.assertEqual(anagrams(), 'NOT ANAGRAM')
	def test_three(self):
		user_input = 'BRADE beard'
		with patch('builtins.input', return_value = user_input):
			self.assertEqual(anagrams(), 'ANAGRAM')

class TestCreditCard(unittest.TestCase):
	def test_one(self):
		n = 79927398713
		res = is_credit_card_valid(n)
		self.assertEqual(res, '79927398713 is a valid number')
	def test_two(self):
		n = 79927398715
		res = is_credit_card_valid(n)
		self.assertEqual(res, '79927398715 is invalid number')

class TestGoldbach(unittest.TestCase):
	def test_one(self):
		res = goldbach(4)
		self.assertEqual(res, [(2,2)])
	def test_two(self):
		res = goldbach(6)
		self.assertEqual(res, [(3,3)])
	def test_three(self):
		res = goldbach(8)
		self.assertEqual(res, [(3,5)])
	def test_four(self):
		res = goldbach(10)
		self.assertEqual(res, [(3,7),(5,5)])
	def test_five(self):
		res = goldbach(100)
		self.assertEqual(res, [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)])

class TestBombing(unittest.TestCase):
	def test(self):
		m = [[1,2,3],[4,5,6],[7,8,9]]
		res = matrix_bombing_plan(m)
		self.assertEqual(res, {(0, 0): 42,(0, 1): 36, (0, 2): 37, (1, 0): 30, (1, 1): 15, (1, 2): 23, (2, 0): 29, (2, 1): 15, (2, 2): 26})
		

if __name__ == '__main__':
	unittest.main()
		