''' Kadane's Algorithm - dynamic programming'''
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