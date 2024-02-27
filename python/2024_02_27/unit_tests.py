import unittest
import random
from binary_search import do_bs


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        n = 10000
        arr = random.sample(range(100000), n)
        arr.sort()
        #print(arr)
        for i, num in enumerate(arr):
            ans = do_bs(arr, num)
            self.assertEqual(i, ans, " " + str(num))


if __name__ == '__main__':
    unittest.main()