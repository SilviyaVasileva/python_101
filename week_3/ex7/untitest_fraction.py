import unittest
from fraction import Fractions, sort


class TestFraction(unittest.TestCase):
	def test_simplify_one(self):
		num1 = Fractions(2,6)
		self.assertEqual(num1, Fractions(1,3))
	def test_simplify_two(self):
		num1 = Fractions(3,9)
		self.assertEqual(num1, Fractions(1,3))
	def test_simplify_three(self):
		num1 = Fractions(1,7)
		self.assertEqual(num1, Fractions(1,7))
	def test_simplify_four(self):
		num1 = Fractions(4,10)
		self.assertEqual(num1, Fractions(2,5))
	def test_simplify_five(self):
		num1 = Fractions(462,63)
		self.assertEqual(num1, Fractions(22,3))

	def test_add_one(self):
		num1 = Fractions(2,6)
		num2 = Fractions(1,7)
		self.assertEqual(num1+num2, Fractions(10,21))
	def test_add_two(self):
		num1 = Fractions(1,4)
		num2 = Fractions(1,2)
		self.assertEqual(num1+num2, Fractions(3,4))
	def test_sort_one(self):
		arr = [Fractions(1,3),Fractions(1,4)]
		res = sorted(arr)
		self.assertEqual(res, [Fractions(1,4),Fractions(1,3)])
	def test_sort_two(self):
		arr = [Fractions(2,3),Fractions(2,4)]
		res = sorted(arr)
		self.assertEqual(res, [Fractions(1,2),Fractions(2,3)])
	def test_sort_three(self):
		arr = [Fractions(2,3),Fractions(1,2), Fractions(1,3)]
		res = sorted(arr)
		self.assertEqual(res, [Fractions(1,3),Fractions(1,2),Fractions(2,3)])
	def test_sort_more(self):
		arr = [Fractions(5, 6), Fractions(22, 78), Fractions(22, 7), Fractions(7, 8), Fractions(9, 6), Fractions(15, 32)]
		res = sorted(arr)
		self.assertEqual(res, [Fractions(22, 78), Fractions(15, 32), Fractions(5, 6), Fractions(7, 8), Fractions(9, 6), Fractions(22, 7)])



if __name__ == '__main__':
	unittest.main()