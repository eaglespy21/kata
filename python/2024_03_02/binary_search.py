def do_bs(arr, k):
    left = 0
    right = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def do_bs_r(arr, k, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        return do_bs_r(arr, k, left, mid - 1)
    else:
        return do_bs_r(arr, k, mid + 1, right)
