def subarraySum(nums, k):
    '''
    Given an array of integers nums and an integer k, 
    return the total number of continuous subarrays whose sum equals to k
    '''
    if not nums:
        return 0
    prefixSum = {0:1}
    result = 0
    curSum = 0
    for num in nums:
        curSum += num
        diff = curSum - k
        result += prefixSum.get(diff, 0)
        prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        
    return result
    
'''
123  k=3
  ^
1 
curSum = 1
diff = 1 - 3 = -2
result += 0 (-1 not in map)
add curSum (1) to map
map = {0:1, 1:1}

2
curSum = 1 + 2 = 3
diff = 3 - 3 = 0
result = 0 + 1 (1 is in map and map[1] = 1)
add 3 to map
map = {0: 1, 1: 1, 3 : 1}

3
curSum = 1 + 2 + 3 = 6
diff = 6 - 3 = 3
result = 1 + 1 (3 is in map, map[3] = 1)
add curSum(6) to map
map = {0: 1, 1: 1, 3 : 1, 6:1}

end of array, return result = 2

'''