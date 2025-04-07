def bs(arr, se):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < se:
            low = mid + 1
        elif arr[mid] > se:
            high = mid - 1
        else:
            return mid
    return -1


def bs(arr, low, high, se):
    mid = (low + high) // 2
    if low > high:
        return -1
    if arr[mid] < se:
        return bs(arr, mid + 1, high, se)
    elif arr[mid] > se:
        return bs(arr, low, mid - 1, se)
    else:
        return mid


'''
PS C:\Projects\kata> cd .\python\2025_04_06\
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from bs import bs
>>> arr = [1,2,3]
>>> bs(arr, 1)
0
>>> bs(arr, 2)
1
>>> bs(arr, 3)
2
>>> bs(arr, 4)
-1
>>> exit()
PS C:\Projects\kata\python\2025_04_06> python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from bs import bs
>>> arr = [1,2,3]
>>> bs(arr, 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bs() missing 2 required positional arguments: 'high' and 'se'
>>> high = len(arr) - 1
>>> bs(arr, 0, high, 1)
0
>>> bs(arr, 0, high, 2)
1
>>> bs(arr, 0, high, 3)
2
>>> bs(arr, 0, high, 4)
-1
'''