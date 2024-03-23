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


def bs_r(arr, left, right, k):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] > k:
        return bs_r(arr, left, mid - 1, k)
    elif arr[mid] < k:
        return bs_r(arr, mid + 1, right, k)
    else:
        return mid
