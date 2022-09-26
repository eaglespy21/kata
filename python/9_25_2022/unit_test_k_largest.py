from random import sample
import unittest
from k_largest import do_k_largest


class KLargestTestCase(unittest.TestCase):
    def test_do_k_largest(self):
        arr = sample(range(0, 10000), 9000)
        k = 10
        res = do_k_largest(arr, k)
        arr.sort(reverse=True)
        for num in res:
            self.assertIn(num, arr[:k], f'res: {res}, arr: {arr[:k]}')


if __name__ == '__main__':
    unittest.main()