import unittest
import random
from binary_search import doBS, doBSR
from k_largest import getKLargest


class TestAll(unittest.TestCase):

    def testBinarySearch(self):
        n = 100000
        arr = random.sample(range(0, 10000000), n)
        arr.sort()
        arrLen = len(arr)
        for i, num in enumerate(arr):
            self.assertEqual(i, doBS(arr, num))
            self.assertEqual(i, doBSR(arr, num, 0, arrLen))

    def testKLargest(self):
        n = 10
        k = 5
        arr = random.sample(range(0, 1000000), n)
        ans = getKLargest(arr, k)
        arr.sort(reverse=True)
        self.assertEqual(ans, arr[:k])



if __name__ == '__main__':
    unittest.main()
