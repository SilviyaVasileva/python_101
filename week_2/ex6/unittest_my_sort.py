import unittest
from my_sort import sort

class TetsMySort(unittest.TestCase):
    def test_sort_with_arr_without_arg(self):
        arr = []
        res = sort(arr)
        self.assertEqual(res, [])
    
    
    def test_sort_with_arr_reverce_true(self):
        arr = [2,4,1]
        res = sort(interable = arr)
        self.assertEqual(res, [1,2,4])
    
    def test_sort_with_arr_reverce_falce(self):
        arr = [2,4,1]
        res = sort(interable = arr, ascending = False)
        self.assertEqual(res, [4,2,1])
        
    def test_sort_with_arr_of_dict(self):
        arr = [{'a':2},{'a':4},{'a':1}]
        res = sort(interable = arr, ascending = False)
        self.assertEqual(res, [{'a':1},{'a':2},{'a':4}])

        
    def test_sort_with_arr_of_dict_with_key(self):
        arr = [{'a':5,'b':2},{'a':4,'b':1},{'a':1, 'b':3}]
        res = sort(interable = arr, ascending = True, keY = 'b')
        self.assertEqual(res, [{'a':1, 'b':3},{'a':5,'b':2},{'a':4,'b':1}])
                



if __name__ == '__main__':
    unittest.main()