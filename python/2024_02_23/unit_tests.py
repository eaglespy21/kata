import unittest
import random
from binary_search import do_binary_search


class TestBinarySearch(unittest.TestCase):
    #TODO: Handle duplicates
    def testBinarySearch(self):
        arr = [random.randrange(0, 100) for _ in range(10)]
        arr.sort()
        print(arr)
        k = 6
        ans = do_binary_search(arr, arr[k])
        self.assertEquals(k, ans)


if __name__ == '__main__':
    unittest.main()
