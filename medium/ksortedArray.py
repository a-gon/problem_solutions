import heapq
def partialSortHeap(input, k):
    heap = input[: k + 1]
    heapq.heapify(heap) # O(k log k)
    cur = 0
    for i in range(k+1, len(input)):   # O(n)
        input[cur] = heapq.heappop(heap)
        cur += 1
        heapq.heappush(heap, input[i])   # O(log k)
        
    while heap:
        input[cur] = heapq.heappop(heap)   # O(log k)
        cur += 1
    
    return input
# total runtime complexity: O(n * log k)
print(partialSortHeap([1,3,2,4,6,5], 2), 'expect [1,2,3,4,5,6]')
