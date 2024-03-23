import unittest
import random
from binary_search import bs


class TestAll(unittest.TestCase):
    def testBinarySearch(self):
        n = 100
        arr = random.sample(range(0, 1000000), n)
        arr.sort()
        for i, num in enumerate(arr):
            self.assertEqual(i, bs(arr, num))


if __name__ == '__main__':
    unittest.main()
