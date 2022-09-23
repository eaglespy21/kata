from random import sample
import unittest
from binary_search import do_binary_search
from k_largest import get_k_largest


class BinarySearchTestCase(unittest.TestCase):

    def test_binary_search(self):
        arr = sample(range(0, 10000), 9000)
        arr.sort()
        for i, num in enumerate(arr):
            res = do_binary_search(arr, num)
            self.assertGreaterEqual(res, 0)
            self.assertEqual(num, arr[res])

    def test_k_largest(self):
        arr = sample(range(0, 10000), 9000)
        k = 5
        # print(arr)
        res = get_k_largest(arr, k)
        arr.sort(reverse=True)
        expected = arr[:k]
        # print(expected, res)
        # self.assertEqual(expected, res)
        for num in expected:
            self.assertIn(num, res, f'res {res}, expected {expected}, arr {arr}')


if __name__ == '__main__':
    unittest.main()  # How to select a test to run in main?
