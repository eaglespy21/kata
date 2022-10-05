from random import sample
import unittest
from binary_search import do_binary_search
from k_largest import do_k_largest
# pylance is screwed up - its referencing the wrong binary search module


class BinarySearchTestCase(unittest.TestCase):

    def test_do_binary_search(self):
        arr = sample(range(0, 100), 100)
        arr.sort()
        for val in arr:
            res = do_binary_search(arr, val)
            self.assertGreaterEqual(res, 0)
            self.assertEqual(arr[res], val)

    def test_do_k_largest(self):
        arr = sample(range(0, 100), 100)
        k = 5
        res = do_k_largest(arr, k)
        arr.sort(reverse=True)
        for i, num in enumerate(arr[:k]):
            self.assertTrue(num in res)


if __name__ == '__main__':
    unittest.main()
