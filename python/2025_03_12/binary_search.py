from random import randrange


def bin_search(arr, k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < k:
            low = mid + 1
        elif arr[mid] > k:
            high = mid - 1
        else:
            return mid
    return -1


arr = [5, 3, 6, 8, 10, 1]
arr.sort()

for i, val in enumerate(arr):
    ans = bin_search(arr, val)
    print(f'index is {i} and value is {val} and ans is {ans}')
    assert i == ans
