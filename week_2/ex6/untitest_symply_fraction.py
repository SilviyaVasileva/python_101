import unittest
from simply_fraction import simplify_fractions

class TestSimplifyFractions(unittest.TestCase):
	def test_with_symple_number(self):
		number = (1,7)
		res = simplify_fractions(number)
		self.assertEqual(res, (1,7))

	def test_with_numbers_with_gcd_three_first_number_is_smaller(self):
		number = (3,9)
		res = simplify_fractions(number)
		self.assertEqual(res, (1,3))

	def test_with_numbers_with_gcd_four_first_number_is_smaller(self):
		number = (8,28)
		res = simplify_fractions(number)
		self.assertEqual(res, (2,7))

	def test_second_number_is_smaller(self):
		number = (462,63)
		res = simplify_fractions(number)
		self.assertEqual(res, (22,3))

if __name__ == '__main__':
	unittest.main()