arr = [1, 2, 3, 4, 5]


def binary_search(arr, key):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    val = binary_search(arr=arr, key=5)
    print(val)


# Things to try next time -
# 1. random sorted numbers
# 2. measure time taken
# 3. add type hints
# 4. add documentation
# 5. accept cmd line arguments
# print(arr)
