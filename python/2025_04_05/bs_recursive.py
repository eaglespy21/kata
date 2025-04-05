arr = [1, 2, 3, 4, 8, 9]


def bs_r(arr, low, high, se):
    mid = (low + high) // 2
    # print(f'{arr, low}, {high}, {se}')
    if low > high:
        return -1
    if arr[mid] == se:
        return mid
    elif arr[mid] < se:
        return bs_r(arr, mid + 1, high, se)
    elif arr[mid] > se:
        return bs_r(arr, low, mid - 1, se)


high = len(arr) - 1
ans = bs_r(arr, 0, high, 9)
print(ans)