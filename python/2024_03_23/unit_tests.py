import unittest
import random
from binary_search import bs


class TestAll(unittest.TestCase):

    def setUp(self):
        n = 100
        self.arr = random.sample(range(0, 1000000), n)
        self.arr.sort()

    def testBinarySearch(self):
        for i, num in enumerate(self.arr):
            self.assertEqual(i, bs(self.arr, num))

    def testBinarySearchR(self):
        for i, num in enumerate(self.arr):
            self.assertEqual(i, bs(self.arr, num))


if __name__ == '__main__':
    unittest.main()
