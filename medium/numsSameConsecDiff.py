def numsSameConsecDiff(n: int, k: int):
    '''
    n=3, k=7
    [1, 2, ]
    can start with:
    1, 2, 7, 8, 9
    second digit:
    18, 29, 70, 81, 92
    third digit:
    181, 292, 707, 818, 929
    
    '''
    nums = []

    def dfs(N, curNum):
        if N == 0:
            return nums.append(curNum)
        
        lastDig = curNum % 10
        nextDigs = set([lastDig + k, lastDig - k])
        for nextDig in nextDigs:
            if 0 <= nextDig < 10:
                dfs(N - 1, curNum * 10 + nextDig)

    
    for i in range(1, 10):
        dfs(n - 1, i)
                        
    return nums



print(numsSameConsecDiff(3, 7), 'expected [181,292,707,818,929]')
