import collections
def combinationSum(self, candidates, target: int):
    if not candidates:
        return []
    
    candidates.sort()
    dp = collections.defaultdict(list)
    dp[0] = [[]]
    for c in candidates:
        for t in range(c, target + 1):
            diff = t - c   # 5 - 3 = 2
            for nums in dp[diff]:   # for num in dp[2]
                dp[t].append(nums + [c])  # dp[5] = [2,3]
                                                    #  ^ 
                
    return dp[target] if target in dp else []
                    