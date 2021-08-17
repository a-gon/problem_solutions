def numSubarraysWithSum(nums, goal: int) -> int:
    '''
    Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
    '''
    result = 0
    curSum = 0
    counter = {}
    for num in nums:  # 1
        curSum += num               # curSum = 3
        if curSum == goal:
            result += 1                                    # result = 2
        result += counter.get(curSum - goal, 0)         #result = 2 + 2 = 4  curSum - goal = 1 counter[1] = 2
        counter[curSum] = counter.get(curSum, 0) + 1    # counter = 1: 2, 2: 1, 3: 1
        
    return result


    