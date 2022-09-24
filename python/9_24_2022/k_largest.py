from copy import deepcopy
import heapq


def find_k_largest(arr, k):
    pq = deepcopy(arr[:k])
    # pq = [x for x in pq]
    heapq.heapify(pq)
    for num in arr[k:]:
        if num > pq[0]:
            heapq.heappushpop(pq, num)
        else:
            pass
    return pq
