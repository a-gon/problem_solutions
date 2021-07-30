def knapsack(limit: int, items) -> int:
    '''
    Example:
    • Given: values = [6, 9, 13], weights = [1, 2, 3], c = 5 // returns 22
    • Note: 9 + 13 (weight: 2 + 3 <= 5)
    5, {1: 6, 2: 9, 3: 13}

          0 1 2  3  4  5
    w__v__________________      
    1: 6  0 6 6  6  6  6
    2: 9  0 6 9 15 15 15 
    3: 13 0 6 9 15 19 22 

    max(13 + 0, 15) = 15
    max(13 + 6, 15) = 19
    max(13 + 9, 15) = 22



    '''


    if not items or not limit:
        return 0
    T = [[0 for j in range(limit + 1)] for i in range(len(items))]
    values = sorted(items.values())
    weights = sorted(items.keys())
    print(values, weights)
    for i in range(len(T)):
        for j in range(1, len(T[0])):
            val = values[i]
            weight = weights[i]
            # cur_weight = j
            if weight > j:
                # current weight is greater than total weight possible, so we exclude curr value (look at the row above)
                T[i][j] = T[i - 1][j]
            else:
                # current weight is <= that total weight possible: 
                # we pick max between (curr value included, curr value excluded)
                # for row 0: max(6 + 0, 0) = 6 (not getting out of bounds in Python, evaluates to T[0-1][..] which is initialied to 0 )
                T[i][j] = max(val + T[i - 1][j - weight], T[i - 1][j])
    print(T)
                
    return T[-1][-1]


print(knapsack(5, {1: 6, 2: 9, 3: 13}))