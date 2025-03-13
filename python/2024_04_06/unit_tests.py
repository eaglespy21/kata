import unittest
import random
from binary_search import bs

class TestAll(unittest.TestCase):
    def testBs(self):
        n = 1000
        arr = random.sample(range(1000000), n)
        arr.sort()
        #print(arr)
        for i, num in enumerate(arr):
            ans = bs(arr, num)
            self.assertEqual(num, arr[ans])

if __name__ == '__main__':
    unittest.main()