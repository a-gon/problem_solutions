from collections import deque
def findMedianSortedArrays(self, nums1, nums2) -> float:
    
    # def binaryClosest(array, target):
    #     ''' return one value: target itself or avg between 2 closest values'''
    #     if target <= array[0]:
    #         return array[0]
    #     elif target >= array[-1]:
    #         return array[-1]
    #     lo, hi = 0, len(array) - 1
    #     while lo <= hi:
    #         mid = (lo + hi) // 2
    #         if float(array[mid]) == target:
    #             return float(array[mid])
    #         elif target < array[mid]:
    #             hi = mid - 1
    #         else:
    #             lo = mid + 1
    #     if abs(lo - hi) == 1:
    #         return (array[lo] + array[hi]) / 2
        
    def mergeArrays(nums1, nums2):
        ''' Merge 2 arrays into 1 sorted array'''
        d1 = deque(nums1)
        d2 = deque(nums2)
        result = []
        while d1 and d2:
            if d1[0] < d2[0]:
                result.append(d1.popleft())
            else:
                result.append(d2.popleft())
        result = result + (list(d1) or list(d2))
        
        return result

    merged_array = mergeArrays(nums1, nums2)
    if len(merged_array) % 2 == 1:
        mid_idx = len(merged_array) // 2
        median = merged_array[mid_idx]
    else:
        mid_idx = len(merged_array) // 2
        median = (merged_array[mid_idx] + merged_array[mid_idx - 1]) / 2
    
    return median
    

