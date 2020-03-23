import unittest
from sort_fractions import sort_fraction

class TestSortFractions(unittest.TestCase):
	def test_with_same_denominator(self):
		arr = [(2,3),(1,3)]
		res = sort_fraction(arr)
		self.assertEqual(res, [(1,3),(2,3)])
	def test_with_two_fractions(self):
		arr = [(2,3),(1,2)]
		res = sort_fraction(arr)
		self.assertEqual(res, [(1,2),(2,3)])
	def test_with_three_fractions(self):
		arr = [(2,3),(1,2),(1,3)]
		res = sort_fraction(arr)
		self.assertEqual(res, [(1,3),(1,2),(2,3)])
	def test_with_more_fractions(self):
		arr = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
		res = sort_fraction(arr)
		self.assertEqual(res, [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)])


if __name__ == '__main__':
	unittest.main()