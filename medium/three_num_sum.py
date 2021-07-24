def threeNumberSum(array, targetSum):
    '''
    Takes in array of nums and returns a list of triplets with sum = targetSum.
    The number in the triplets are ordered in asc order, 
    and the triplets themselves rea ordered in asc order. 
    '''
    result = []
    array.sort()

    def backtrack(array, cur_nums, result):
        if len(cur_nums) > 3:
            return
        if len(cur_nums) == 3 and sum(cur_nums) == targetSum:
            return result.append(cur_nums)

        for i in range(len(array)):
            backtrack(array[i + 1:], cur_nums + [array[i]], result)
	
	backtrack(array, [], result)
	return result




def threeNumberSum(array, targetSum):
    '''
    Same problem, more optimal approach, using three pointers.
    Time: O(N^2)
    Space: O(N)
    '''
    result = []
    array.sort()
    for i in range(len(array)):
        left = i + 1
        right = len(array) - 1
        while left < right:
            curSum = array[i] + array[left] + array[right]
            if curSum == targetSum:
                result.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif curSum < targetSum:
                left += 1
            else:
                right -= 1
                
    return result