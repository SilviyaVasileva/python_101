import unittest
from ex2 import gas_station, is_number_balanced, increasing_or_decreasing,\
get_largest_palindrom, sum_of_numbers, birthday_ranges

class TestGasStation(unittest.TestCase):
	def test_one(self):
		res = gas_station(320, 90, [50, 80, 140, 180, 220, 290])
		self.assertEqual(res, [80,140,220,290])
	def test_two(self):
		res = gas_station(390, 80, [70, 90, 140, 210, 240, 280, 350])
		self.assertEqual(res, [70, 140, 210, 280, 350])

class TestIsNumberBalanced(unittest.TestCase):
	def test_with_one_digit_number(self):
		res = is_number_balanced(4)
		self.assertTrue(res)
	def test_with_nt_balanced_number(self):
		res = is_number_balanced(1234)
		self.assertFalse(res)
	def test_with_odd_digits(self):
		res = is_number_balanced(1238033)
		self.assertTrue(res)
	def test_with_even_digits(self):
		res = is_number_balanced(1423)
		self.assertTrue(res)

class TestIncreasingDecreasing(unittest.TestCase):
	def test_with_incr(self):
		res = increasing_or_decreasing([1,2,3,6,7,8])
		self.assertEqual(res,'up')
	def test_with_decr(self):
		res = increasing_or_decreasing([15,6,2,1,-4])
		self.assertEqual(res,'down')
	def test_with_same_num(self):
		res = increasing_or_decreasing([1,1,1,1,1])
		self.assertFalse(res)
	def test_false(self):
		res = increasing_or_decreasing([1,5,-11,21,15])
		self.assertFalse(res)

class TestLargestPalindrom(unittest.TestCase):
	def test_10(self):
		res = get_largest_palindrom(10)
		self.assertEqual(res, 9)
	def test_100(self):
		res = get_largest_palindrom(100)
		self.assertEqual(res, 99)
	def test_1000(self):
		res = get_largest_palindrom(1000)
		self.assertEqual(res, 999)
	def test_99(self):
		res = get_largest_palindrom(99)
		self.assertEqual(res, 88)
	def test_252(self):
		res = get_largest_palindrom(252)
		self.assertEqual(res, 242)
	def test_994687(self):
		res = get_largest_palindrom(994687)
		self.assertEqual(res, 994499)
	def test_9439(self):
		res = get_largest_palindrom(9439)
		self.assertEqual(res, 9339)
	def test_754649(self):
		res = get_largest_palindrom(754649)
		self.assertEqual(res, 754457)

class TestSumNumber(unittest.TestCase):
	def test_with_string(self):
		res = sum_of_numbers('asdf')
		self.assertEqual(res, 0)
	def test_with_number(self):
		res = sum_of_numbers('1101')
		self.assertEqual(res, 1101)
	def test_with_string_and_number(self):
		res = sum_of_numbers('ab12')
		self.assertEqual(res, 12)
	def test_with_strings_and_numbers_one(self):
		res = sum_of_numbers('ab125cd3')
		self.assertEqual(res, 128)
	def test_with_strings_and_numbers_two(self):
		res = sum_of_numbers('1111O')
		self.assertEqual(res, 1111)
	def test_with_strings_and_numbers_three(self):
		res = sum_of_numbers('1abc33xyz22')
		self.assertEqual(res, 56)
	def test_with_strings_and_numbers_zero(self):
		res = sum_of_numbers('as0df')
		self.assertEqual(res, 0)
		
class TestBDayRange(unittest.TestCase):
	def test_one(self):
		res = birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)])
		self.assertEqual(res, [2,3,4,5,2])
	def test_two(self):
		res = birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)])
		self.assertEqual(res, [5,2,0,1])
		





if __name__ == '__main__':
			unittest.main()		