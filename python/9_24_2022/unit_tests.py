from random import sample
from k_largest import find_k_largest

import unittest


class KLargestTestCase(unittest.TestCase):
    def test_find_k_largest(self):
        arr = sample(range(0, 10000), 9000)
        k = 5
        res = find_k_largest(arr, k)
        arr.sort(reverse=True)
        for num in res:
            self.assertIn(num, arr[:k])
        # Test for duplicates case


if __name__ == '__main__':
    unittest.main()
