import unittest
import random
from binary_search import doBS, doBSR


class TestBinarySearch(unittest.TestCase):

    def testBinarySearch(self):
        n = 100000
        arr = random.sample(range(0, 10000000), n)
        arr.sort()
        arrLen = len(arr)
        for i, num in enumerate(arr):
            self.assertEqual(i, doBS(arr, num))
            self.assertEqual(i, doBSR(arr, num, 0, arrLen))


if __name__ == '__main__':
    unittest.main()
