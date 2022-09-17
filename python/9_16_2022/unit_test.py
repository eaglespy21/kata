import unittest
from random import sample
from binary_search import do_binary_search


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        arr = [1, 2, 3, 4, 5]
        val = 5
        res = do_binary_search(arr, val)
        self.assertGreaterEqual(res, 0)
        self.assertEqual(arr[res], val)

    def test_random_numbers(self):
        arr = sample(range(0, 10000), 10000)
        arr.sort()
        for i, val in enumerate(arr):
            res = do_binary_search(arr, val)
            self.assertGreaterEqual(res, 0)
            self.assertEqual(val, arr[res])


if __name__ == '__main__':
    unittest.main()
