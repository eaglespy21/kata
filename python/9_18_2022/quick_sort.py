from random import randrange


def do_quick_sort(arr):
    left = 0
    right = len(arr)
    for i in range(2):
        pivot = randrange(0, len(arr))
        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] > arr[pivot] and arr[right] <= arr[pivot]:
                arr[left], arr[right] = arr[right], arr[left]
            else:
                if arr[left] <= arr[pivot]:
                    left += 1
                if arr[right] > arr[pivot]:
                    right -= 1
        arr[pivot], arr[left] = arr[left], arr[pivot]





