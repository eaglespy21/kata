def do_bs(arr, k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
    return -1