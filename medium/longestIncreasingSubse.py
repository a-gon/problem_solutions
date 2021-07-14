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

        
def longestIncreasingSubsequence(array):
    ''' Another solution, more efficient in terms of space - sttores onle the indices needed for recreating the resulting sequence'''
    if not array:
	    return array
    lengths = [1] * len(array)
    sequences = [None] * len(array)
    maxLenIdx = 0
    for i in range(len(array)):
	    for j in range(i):
		    if array[j] < array[i] and lengths[j] + 1 >= lengths[i]:
			    lengths[i] = lengths[j] + 1
			    sequences[i] = j
	    if lengths[i] >= lengths[maxLenIdx]:
		    maxLenIdx = i

    return buildSeqs(array, sequences, maxLenIdx)

def buildSeqs(array, sequences, startIdx):
	result = []
	while startIdx is not None:
		result.append(array[startIdx])
		startIdx = sequences[startIdx]
	return list(reversed(result))


assert(longestIncreasingSubsequence([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]) == [-24, 2, 3, 5, 6, 35]), 'Incorrect result in test case 1'
assert(longestIncreasingSubsequence([3, 2, 1]) == [3] or [1] or [2]), 'Incorrect result in test case 2'
