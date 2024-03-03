import heapq


def getKLargest(arr, k):
    # print(arr)
    # arr = [-1 * num for num in arr]
    # print(arr)
    # heapq.heapify(arr)
    # print(arr)
    return heapq.nlargest(k, arr)