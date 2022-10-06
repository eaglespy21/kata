import heapq


def do_k_largest(arr, k):
    pq = arr[:k]
    heapq.heapify(pq)
    for num in arr[k:]:
        if num > pq[0]:
            heapq.heappushpop(pq, num)
    return pq