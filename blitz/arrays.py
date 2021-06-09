def bubbleSort(array: [int]) -> [int]:
    noSwap = True
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                noSwap = False
        if noSwap:
            break
    return array

# Test Cases
print("Bubble sort:")
print(bubbleSort([])) # []
print(bubbleSort([1])) # [1]
print(bubbleSort([3, 1, 2, 4])) # [1, 2, 3, 4]
print(bubbleSort([-10, 1, 3, 8, -13, 32, 9, 5])) # [-13, -10, 1, 3, 5, 8, 9, 32]


def selectionSort(array: [int]) -> [int]:
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
    return array
# Test Cases
print('Selection Sort:')
print(selectionSort([])) # []
print(selectionSort([1])) # [1]
print(selectionSort([3, 1, 2, 4])) # [1, 2, 3, 4]
print(selectionSort([-10, 1, 3, 8, -13, 32, 9, 5])) # [-13, -10, 1, 3, 5, 8, 9, 32]

def insertionSort(array: [int]) -> [int]:
    for i in range(len(array)):
        j = i
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array

# Test Cases
print('Insertion Sort:')
print(insertionSort([])) # []
print(insertionSort([1])) # [1]
print(insertionSort([3, 1, 2, 4])) # [1, 2, 3, 4]
print(insertionSort([-10, 1, 3, 8, -13, 32, 9, 5])) # [-13, -10, 1, 3, 5, 8, 9, 32]


def merge(arr1, arr2):
    result = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
    while arr1:
        result.append(arr1.pop(0))
    while arr2:
        result.append(arr2.pop(0))

    return result

def mergeSort(array: [int]) -> [int]:
    if not array:
        return array
    if len(array) == 1:
        return array
    arr1 = array[ : len(array)//2]
    arr2 = array[len(array)//2 : ]
    arr1 = mergeSort(arr1)
    arr2 = mergeSort(arr2)

    return merge(arr1, arr2)

# Test Cases
print(mergeSort([])) # []
print(mergeSort([1])) # [1]
print(mergeSort([3, 1, 2, 4])) # [1, 2, 3, 4]
print(mergeSort([-10, 1, 3, 8, -13, 32, 9, 5])) # [-13, -10, 1, 3, 5, 8, 9, 32]

def firstKTimes(array: [int], k: int) -> int:
    counts = {}
    for i in array:
        new_count = counts.get(i, 0) + 1
        if new_count == k:
            return i
        counts[i] = new_count
    return -1

# Test Cases
print('Find first element that repeats k times:')
print(firstKTimes([1, 2, 2, 3, 3], 2)) # 2
print(firstKTimes([1, 2, 2, 3, 3], 4)) # -1
print(firstKTimes([], 1)) # -1

def numUniques(array: [int]) -> int:
    counts = {}
    result = 0
    for i in array:
        new_count = counts.get(i, 0) + 1
        if new_count == 1:
            result += 1
        counts[i] = new_count
    return result

# Test Cases
print('Num unique elements:')
print(numUniques([])) # 0
print(numUniques([3, 1, 1, 2, 3, 1, 1, 1, 4])) # 4
print(numUniques([1])) # 1

def numNonDuplicated(array: [int]) -> int:
    counts = {}
    result = 0
    for i in array:
        new_count = counts.get(i, 0) + 1
        if new_count == 1:
            result += 1
        elif new_count == 2:
            result -= 1
        counts[i] = new_count
    return result

# Test Cases
print('Num elements that do not repeat:')
print(numNonDuplicated([])) # 0
print(numNonDuplicated([3, 1, 1, 2, 3, 1, 1, 1, 4])) # 2
print(numNonDuplicated([1])) # 1
print(numNonDuplicated([1,1,1,1])) # 1


def numDuplicates(array: [int]) -> int:
    counts = {}
    result = 0
    for i in array:
        new_count = counts.get(i, 0) + 1
        if new_count == 2:
            result += 1
        counts[i] = new_count
    return result

# Test Cases
print('Num duplicated elements:')
print(numDuplicates([])) # 0
print(numDuplicates([3, 1, 1, 2, 3, 1, 1, 1, 4])) # 2
print(numDuplicates([1])) # 0


def binarySearch(array: [int], target: int) -> int:
    low, hi = 0, len(array)-1
    while low <= hi:
        mid = (low + hi) // 2
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            hi = mid - 1
        else:
            low = mid + 1
    return -1

# Test Cases
array = [1, 2, 3, 6, 8, 13, 113, 153, 200]
print('Binary search:')
print(binarySearch(array, 1)) # 0
print(binarySearch(array, 200)) # 8
print(binarySearch(array, 8)) # 4
print(binarySearch(array, 154)) # -1