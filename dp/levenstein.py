def levenshteinDistance(str1, str2):

	'''
    Given two strings, return the minimum number of edits needed to turn str1 into str2. Edits are: insert, delete, replace character

	  '' a b c
	 ----------
	'' 0 1 2 3
	 y 1 1 2 3
	 a 2 1 2 3 
	 b 3 2 1 2
	 d 4 3 2 2
	
	'''
	T = [[j for j in range(len(str1) + 1)] for i in range(len(str2) + 1)]
	for i in range(len(str2) + 1):
		T[i][0] = i
	for i in range(1, len(str2) + 1):
		for j in range(1, len(str1) + 1):
			if str2[i - 1] == str1[j - 1]:
				T[i][j] = T[i - 1][j - 1]
			else:
				T[i][j] = 1 + min(T[i - 1][j], T[i][j - 1], T[i - 1][j - 1])
	return T[-1][-1]