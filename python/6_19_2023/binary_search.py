# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

import random 
from math import ceil 

def unit_test():
    arr = random.sample(range(0, 1000), 10)
    print(arr)
    arr.sort()
    print(arr)
    for i, key in enumerate(arr):
        found_i = bin_search(arr, key, True)
        print(found_i, i)
        assert found_i == i 

def bin_search(arr, key, is_sorted=False):
    #Verify the array is sorted 
    if not is_sorted:
        arr.sort()
    left = 0
    right = len(arr)
    while left < right:
        mid = (right + left) // 2
        print(left, right, mid, arr[mid])
        if arr[mid] == key:
            return mid 
        elif arr[mid] < key:
            left = mid + 1
        elif arr[mid] > key:
            right = mid - 1
        else:
            print("not possible")
    return -1 
    
unit_test()
