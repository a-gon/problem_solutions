def queensAttacktheKing(queens, king):
    if not queens or not king:
        return []

    directions = [-1,0,1]
    result = []
    for i in directions:
        for j in directions:
            if (i == 0 and j == 0):
                continue
            nx = king[0] + i
            ny = king[1] + j
            
            while  0 <= nx < 8 and  0 <= ny<8:
                if [nx,ny] in queens:
                    result.append([nx, ny])
                    break
                nx += i
                ny += j    
                    
            
    return result  