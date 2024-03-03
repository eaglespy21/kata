import unittest
import random
from binary_search import do_bs, do_bs_r


class TestBinarySearch(unittest.TestCase):

    def testBinarySearch(self):
        n = 1000
        arr = random.sample(range(0, 100000), n)
        arr.sort()
        for i, num in enumerate(arr):
            self.assertEqual(i, do_bs(arr, num))

    def testBinarySearchRecursive(self):
        n = 1000
        arr = random.sample(range(0, 100000), n)
        arr.sort()
        for i, num in enumerate(arr):
            ans = do_bs_r(arr, num, 0, len(arr))
            self.assertEqual(i, ans)


if __name__ == '__main__':
    unittest.main()