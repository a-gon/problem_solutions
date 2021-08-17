import collections
from heapq import heappush, heappop
def reorganizeString(s: str) -> str:
    if len(s) <= 1:
        return s
    counts = collections.Counter(s)
    heap = []
    for char, freq in counts.items():
        heappush(heap, (-freq, char))
    result = ''
    
    while len(heap) > 1:
        f1, c1 = heappop(heap)
        f2, c2 = heappop(heap)
        
        result += c1
        result += c2
        if abs(f1) > 1:
            heappush(heap, (f1 + 1, c1))
        if abs(f2) > 1:
            heappush(heap, (f2 + 1, c2))
        
    if heap:
        f, c = heappop(heap)
        if abs(f) > 1:
            return ''
        else:
            result += c
    
    return result      


print(reorganizeString('aab'), 'expect aba')
print(reorganizeString('aaab'), 'expect \'\' ')