''' Kadane's Algorithm'''
def kadanesAlgorithm(array):
    ''' Finds max sum of a subarray
    "array": [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4] 
    output: 19 // [1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1]   
    O(n) time, O(1) space
    '''
    cur_sum = array[0]
    max_sum = cur_sum
    for num in array[1:]:
	    cur_sum = max(cur_sum + num, num)
	    max_sum = max(max_sum, cur_sum)
    return max_sum

def maxSumSubarray(array):
    ''' Return the actual subarray containing the max sum'''
    cur_sum = array[0]
    max_sum = cur_sum
    ref = {}
    cur_subarr = [array[0]]
    for num in array[1:]:
        if cur_sum + num > cur_sum:
            cur_subarr.append(num)
            cur_sum += num

        else:
            ref[cur_sum] = cur_subarr
            cur_sum = num
            cur_subarr = [num]
        # ref[cur_sum] = cur_subarr
        if cur_sum > max_sum:
            max_sum = cur_sum
            # ref[max_sum] = cur_subarr

    print(ref)
    max_subarray = ref[max_sum]


    return max_subarray

print(maxSumSubarray([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4] ))








def sortColors(nums):
    """
    Given ar array of 0s, 1s and 2s, group them all in ascending order
    AKA Dutch national flag problem
    """
    left = 0            # right boundary of zeros
    right = len(nums) - 1   # left boundary of twos
    cur = 0                 # current element
    while cur <= right:
        if nums[cur] == 0:
            nums[cur], nums[left] = nums[left], nums[cur]
            left += 1
            cur += 1
        elif nums[cur] == 2:
            nums[cur], nums[right] = nums[right], nums[cur]
            right -= 1
        else:
            cur += 1
    return nums

    """
    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    """