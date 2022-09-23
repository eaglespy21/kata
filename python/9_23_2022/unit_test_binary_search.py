from random import sample
import unittest
from binary_search import do_binary_search


class BinarySearchTest(unittest.TestCase):

    def test_binary_search(self):
        arr = sample(range(0, 10000), 9000)
        arr.sort()
        for i, num in enumerate(arr):
            res = do_binary_search(arr, num)
            self.assertGreaterEqual(res, 0)
            self.assertEqual(num, arr[res])


if __name__ == '__main__':
    unittest.main()
