import unittest
import random
from binary_search import bs, bs_r
import hug
import endpoints


class TestAll(unittest.TestCase):

    def setUp(self):
        n = 100
        self.arr = random.sample(range(0, 1000000), n)
        self.arr.sort()

    def testBinarySearch(self):
        for i, num in enumerate(self.arr):
            self.assertEqual(i, bs(self.arr, num))
        self.assertEqual(-1, bs(self.arr, -99))

    def testBinarySearchR(self):
        for i, num in enumerate(self.arr):
            self.assertEqual(i, bs_r(self.arr, 0, len(self.arr), num))
        self.assertEqual(-1, bs_r(self.arr, 0, len(self.arr), -99))

    def testHugAPIs(self):
        response = hug.test.get(endpoints, 'add_num', {'a': ['1', '2', '3']})
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data, 'arr is []')


if __name__ == '__main__':
    unittest.main()
