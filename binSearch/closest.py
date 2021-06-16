def binarySearchClosest(array1, target):
    if not array1:
        return -1
    if target <= array1[0]:
        return array1[0]
    if target >= array1[-1]:
        return array1[-1]

    left, right = 0, len(array1) - 1
    while left <= right:
        mid = (left + right) // 2
        print(f'mid: {array1[mid]}')
        if array1[mid] == target:
            return array1[mid]
        elif target < array1[mid]:
            right = mid -1
        else:
            left = mid  + 1
    return array1[left] if abs(array1[left] - target) < abs(array1[right] - target) else array1[right]
    
input = [1, 2, 2, 3, 4, 5, 8, 10, 11, 27, 34, 221, 222]
target = 35
print(binarySearchClosest(input, target))