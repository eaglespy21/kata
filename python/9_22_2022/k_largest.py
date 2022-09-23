from copy import deepcopy
import heapq


def get_k_largest(arr, k):
    arr_copy = deepcopy(arr)
    arr_copy = [x * -1 for x in arr_copy]
    heapq.heapify(arr_copy)
    res = []
    for i in range(k):
        res.append(heapq.heappop(arr_copy) * -1)
    return res
