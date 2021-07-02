'''You given a total number of dice, the number of faces on each dice and a total, write a function that determines the total number of ways to throw the dice to get the target sum.
If the number of faces on a dice is X, then numbers on each face will be 1, 2, ..., X. So a dice with 5 faces will have numbers 1, 2, 3, 4 and 5.
Examples
n = 1, faces = 6, total = 3 returns 1 (must throw face 3)
n = 3, faces = 6, total = 7 returns 15
Spoiler examples (reveals expected questions)
n = 2, faces = 5, total = 8 returns  3 (4, 4 or 3, 5 or 5, 3)'''


memo = {}
def getMemoVal(d, f, t):
    val = '-'.join([str(d), str(f), str(t)])
    return memo.get(val, None)

def setMemo(d, f, t, result):
    memo['-'.join([str(d), str(f), str(t)])] = result

def numRolls(dice, faces, total):
    if dice == 0:
        return 1 if total == 0 else 0

    memo_val = getMemoVal(dice, faces, total)
    if memo_val:
        return memo_val

    result = 0
    for num in range(1, faces + 1):
        result += numRolls(dice - 1, faces, total - num)
    setMemo(dice, faces, total, result)

    return result


print(numRolls(0, 5, 0), 'expected 1')
print(numRolls(3, 6, 7), 'expected 15')
print(numRolls(2, 5, 8), 'expected 3')

