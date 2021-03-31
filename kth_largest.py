import heapq
def kth_largest(a, k):
    heapq.heapify(a)
    result = None
    for _ in range(k):
        result = heapq.heappop(a)
    return result


def kth_largest_(a, k):
    result = None
    sorted_array = sorted(a)
    for _ in range(k):
        result = sorted_array.pop(0)
    return result

print(kth_largest([5,6,31,7,9,25,1,4], 3))
print(kth_largest_([5,6,31,7,9,25,1,4], 3))