import unittest
import random
from binary_search import do_bs


class TestAll(unittest.TestCase):

    def test_bs(self):
        arr = random.sample(range(0, 1000000), 10000)
        arr.sort()
        for i, num in enumerate(arr):
            self.assertEqual(i, do_bs(arr, num))

    # TODO: Missing negative test!!


if __name__ == '__main__':
    unittest.main()