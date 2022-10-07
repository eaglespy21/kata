import heapq

def do_k_largest(arr, k):
    pq = arr[:k]
    heapq.heapify(pq)
    for num in arr[k:]:
        if arr[num] > pq[0]:
            heapq.heappushpop(pq, arr[num])
    return pq