import unittest
from collect_fractions import collect_fraction

class TestCollectFractions(unittest.TestCase):
	def test_nz(self):
		num1 = (1,2)
		num2 = (1,2)

		res = collect_fraction(num1,num2)
		self.assertEqual(res, (1,1))

	def test_nz1(self):
		num1 = (1,2)
		num2 = (1,4)

		res = collect_fraction(num1,num2)
		self.assertEqual(res, (3,4))

	def test_nz2(self):
		num1 = (1,7)
		num2 = (2,6)

		res = collect_fraction(num1,num2)
		self.assertEqual(res, (10,21))

if __name__ == '__main__':
    unittest.main()