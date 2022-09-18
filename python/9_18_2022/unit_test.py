from quick_sort import do_quick_sort
from unittest import TestCase, main


class QuickSortTestcase(TestCase):
    def test_quick_sort(self):
        arr = [5, 4, 3, 2, 1]
        do_quick_sort(arr)
        for i, num in enumerate(arr[:-1]):
            self.assertGreaterEqual(arr[i+1], num)
        print(arr)


if __name__ == '__main__':
    main()
