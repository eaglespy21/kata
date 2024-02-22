import unittest


def binary_search(arr, k):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
    return -1


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        arr = [101, 100, 2, 5, 90, 56]
        arr.sort()
        ans = binary_search(arr, 5)
        self.assertEquals(1, ans)


if __name__ == "__main__":
    unittest.main()
