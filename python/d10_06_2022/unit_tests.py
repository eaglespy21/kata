from random import sample
import unittest
from binary_search import do_binary_search
from k_largest import do_k_largest


class BinarySearchTestCase(unittest.TestCase):
    def test_do_binary_search(self):
        arr = sample(range(0, 100), 100)
        arr.sort()
        for val in arr:
            res = do_binary_search(arr, val)
            self.assertGreaterEqual(res, 0)


class KLargestTestCase(unittest.TestCase):
    def test_do_k_largest(self):
        arr = sample(range(0, 100), 100)
        k = 5
        res = do_k_largest(arr, k)
        arr.sort(reverse=True)
        for num in arr[:k]:
            self.assertIn(num, res)



if __name__ =='__main__':
    unittest.main()