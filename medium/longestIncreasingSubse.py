def longestIncreasingSubseq(array):
    'return the longest increasing sunbsequence of numbers from the array, not necessarily adjacent'
    if len(array) <= 1:
        return array
    T = [[num] for num in array]
    for i in range(1, len(array)):
        for j in range(i):
            if array[j] >= array[i]:
                continue
            T[i] = max(T[i], T[j] + [array[i]], key=lambda x: len(x))

    return max(T, key=lambda x: len(x))


assert(longestIncreasingSubseq([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]) == [-24, 2, 3, 5, 6, 35]), 'Incorrect result in test case 1'
assert(longestIncreasingSubseq([3, 2, 1]) == [3]), 'Incorrect result in test case 2'

        