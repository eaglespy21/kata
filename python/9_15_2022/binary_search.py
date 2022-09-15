from time import time, strftime, localtime
from random import sample


def binary_search(arr, val):
    low = 0
    high = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > val:
            high = mid - 1
        elif arr[mid] < val:
            low = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    arr = sample(range(0, 1000000), 100000)
    arr.sort()
    start = time()
    for ind, i in enumerate(arr):
        res = binary_search(arr=arr, val=arr[ind])
        assert res == ind
    end = time()
    time_taken = end - start
    time_taken = localtime(time_taken)
    time_taken = strftime('%S:%M:%H', time_taken)
    print('success')
    print('time taken = ' + time_taken)
    print('time taken in sec' + str(end-start))
