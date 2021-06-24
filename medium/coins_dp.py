def coinChange(coins: List[int], amount: int) ->int:
    ''' Find min number of coins that in total make up the amount ''' 

        dp = [float('inf')] * (amount + 1)      # array of length amount + 1
        dp[0] = 0                                 
        
        for coin in coins:                       # iterate over coin denominations
            for x in range(coin, amount + 1):       
                dp[x] = min(dp[x], dp[x-coin] + 1)          # how many coins (min) needed to make up the current amount - takes into account the remainder
        return dp[amount] if dp[amount] != float('inf') else -1     # return -1 if 


    '''
        dp approach (bottom up) simulation
    
        coins: 1 2 5
        amount: 11
        dp:
           0 1 2 3 4 5 6 7 8 9 10 11   iterating from i = coin[0] = 1
          -------------------------            coin = 1 (outer loop)
           0 1 2 3 4 5 6 7 8 9 10 11              inner loop: from 1 to 11  
                                                  x = 1, dp[1] = min(inf, dp[1-1] + 1) = min(inf, 1) = 1
                                                  x = 2, dp[2] = min(inf, dp[2-1] + 1) = min(inf, 2) = 2
                                                  x = 3, dp[3] = min(inf, dp[3-1] + 1) = 3
                                                  ...
                                                  x[11], dp[11] = 11
            0 1 2 3 4 5 6 7 8 9 10 11                                       
            -------------------------          coin = 2 (outer loop)
            0 1 1 2 2 3 3 4 4 5 5 6             inner loop: from 2  to 11 
                                                  x = 2, dp[2] = min(dp[2]=2, dp[2-2] + 1) = 1
                                                  x = 3, dp[3] = min(dp[3]=3, dp[1] + 1) =  min(3, 2) = 2
                                                  x = 4, dp[4] = min(4, dp[2] + 1) = min(4, 2) = 2
                                                  x = 5, dp[5] = min(5, dp[3] + 1) = min(5, 3) = 3
                                                  x = 6, dp[6] = min(6, dp[4] + 1) = min(6, 3) = 3
                                                  x = 7, dp[7] = min(7, dp[5] + 1) = min(7, 4) = 4
                                                  x = 8, dp[8] = 4
                                                  x = 9, dp[9] = 5
                                                  x = 10, dp[10] = 5
            0 1 2 3 4 5 6 7 8 9 10 11             x = 11, dp[11] = 6
            -------------------------
            0 1 1 2 2 1 2 2 3 3  2  6          coin = 5 
                                                inner loop: from 5 to 11
                                                    x = 5, dp[5] = min(dp[5]=3, dp[0] + 1) = 1
                                                    x = 6, dp[6] = min(dp[6]=3, dp[1] + 1) = 2
                                                    x = 7, dp[7] = min(dp[7]=4, dp[2] + 1) = 2
                                                    x = 8, dp[8] = min(dp[8]=4, dp[3] + 1) = 3
                                                    x = 9, dp[9] = min(dp[9]=5, dp[4] + 1) = 3
                                                    x = 10, dp[10] = min(dp[10]=5, dp[5] + 1) = 2
                                                    x = 11, dp[11] = min(dp[11]=6, dp[6] + 1) = 3


        coins = [2], amount = 3
        dp = [0 _ _ _] >> [0 _ 1 _ ] >> dp[amount] = inf, so return -1
        test cases:
        [1,2,5], 11 >> 3
        [2], 3  >> -1
        [1], 0 >> 0
        [1], [1] >> 1
        [1], [2] >> 2

        '''
