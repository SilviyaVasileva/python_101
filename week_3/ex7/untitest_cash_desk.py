import unittest
from cash_desk import Bill, BatchBill, CashDesk

class TestBill(unittest.TestCase):
    def test_with_negative_number(self):
        exc = None
        try:
            b = Bill(-5)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), "The amount cannot be negative number!")
    def test_with_string_as_input(self):
        exc = None
        try:
            b = Bill("5")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), "The amount must be integer!")
    def test_with_correct_input_ineger(self):
        b = Bill(5)
        self.assertEqual(int(b), 5)
    def test_with_correct_input_string(self):
        b = Bill(5)
        self.assertEqual(str(b), 'A 5$ bill ')
    def test_with_correct_input_equal_func(self):
        b = Bill(5)
        c = Bill(5)
        self.assertTrue (b == c)
    def test_with_correct_input_equal_func_two(self):
        b = Bill(5)
        a = Bill(55)
        self.assertFalse(b == a)

class TestBatch(unittest.TestCase):
    def test_len_one_element(self):
        b = BatchBill([Bill(10)])
        res = len(b)
        self.assertEqual(res, 1)
    def test_len_two_elements(self):
        b = BatchBill([Bill(30),Bill(10)])
        res = len(b)
        self.assertEqual(res, 2)
    def test_len_odd_elements(self):
        b = BatchBill([Bill(30),Bill(10),Bill(10)])
        res = len(b)
        self.assertEqual(res, 3)
    def test_len_even_elements(self):
        b = BatchBill([Bill(30),Bill(10),Bill(10),Bill(20)])
        res = len(b)
        self.assertEqual(res, 4)
    def test_total_one_element(self):
        b = BatchBill([Bill(30)])
        res = b.total()
        self.assertEqual(res, 30)
    def test_total_two_elements(self):
        b = BatchBill([Bill(30),Bill(10)])
        res = b.total()
        self.assertEqual(res, 40)
    def test_total_three_elements(self):
        b = BatchBill([Bill(30),Bill(10),Bill(10)])
        res = b.total()
        self.assertEqual(res, 50)
    def test_total_more_elements(self):
        b = BatchBill([Bill(30),Bill(10),Bill(10),Bill(23),Bill(110),Bill(15)])
        res = b.total()
        self.assertEqual(res, 198)

class TestCashDesk(unittest.TestCase):
    def test_adding_bill(self):
        d = CashDesk()
        d.take_money(Bill(10))
        self.assertEqual(str(d), str(Bill(10)))
    def test_adding_batch(self):
        d = CashDesk()
        d.take_money(BatchBill([Bill(30),Bill(10),Bill(10)]))
        self.assertEqual(str(d), 'A 30$ bill A 10$ bill A 10$ bill ')
    def test_total(self):
        d = CashDesk()
        d.take_money(BatchBill([Bill(30),Bill(10),Bill(10)]))
        d.take_money(Bill(29))
        self.assertEqual(d.total(), 79)
    def test_inspect(self):
        d = CashDesk()
        d.take_money(BatchBill([Bill(30),Bill(10),Bill(10),Bill(23),Bill(10),Bill(15)]))
        d.take_money(Bill(30))
        res = d.inspect()
        s = res.split('\n')
        self.assertEqual(s,['A 10$ bill 3','A 15$ bill 1','A 23$ bill 1','A 30$ bill 2', ''])

        





if __name__ == '__main__':
    unittest.main()