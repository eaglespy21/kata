def bs(arr, k):
    left = 0
    right = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < k:
            left = mid + 1
        elif arr[mid] > k:
            right = mid - 1
        else:
            return mid
    return -1