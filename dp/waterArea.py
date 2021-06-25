def getWaterArea(heights):
    ''' 
    Given  the list of pillars (their heights), return the area of water trapped between the pillars
    "heights": [0, 1, 0, 1, 0]
    _|_|_    >> water trapped between 1 and 1, height = 1 so area = 1
    approach:
    at each position, calculate the highest pillar to the left of it, and to the right of it (store in arrays)
    
    water area at each point will be equal to min of the left and right highest pillar - 
        minus the height  at curren point (if it's below this min)

    Time complexity: O(n), Space: O(n)

    '''
    max_heights = [0] * len(heights)
    area = 0
    left_max = 0
    for i in range(len(heights)):
        cur_height = heights[i]
        max_heights[i] = left_max
        left_max = max(left_max, cur_height)

    right_max = 0
    for i in reversed(range(len(heights))):
        cur_height = heights[i]
        min_height = min(max_heights[i], right_max)         # find the water level
        if cur_height < min_height:                         # if height at given point is below the water level
            area += min_height - cur_height                 # subtract this piece from area since it's not water, does nothing if there's no pillar
        right_max = max(right_max, cur_height)

    return area


test = [0, 1, 0, 1, 0]
print(getWaterArea(test), 'expected 1')

test = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
print(getWaterArea(test), 'expected 48')

test = [0, 1, 0]
print(getWaterArea(test), 'expected 0')
