def do_binary_search(arr, k):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return -1