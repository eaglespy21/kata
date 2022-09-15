from random import randrange, sample


def binary_search(arr, key):
    low = 0
    high = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > key:
            high = mid - 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            return mid
    return -1


def test_case():  # TODO: Use pytest to run tests, unit_test package
    arr = [1141, 4222, 4320, 4971, 5627, 7428, 7978, 8152, 8265, 9358]
    key = 7
    assert key == binary_search(arr, arr[key])


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    arr = sample(range(0, 10000), 100)
    arr.sort()  # TODO: Replace with quicksort or heapsort, timeit
    key_index = randrange(0, 100)
    # print(arr)
    res = binary_search(arr, arr[key_index])
    print(arr, res, key_index)
    assert key_index == res
    print(res)
    # test_case()
