# /*
#  You're given an array containing either '.', 'L', or 'R' values. These values represent a starting state of a row of dominoes. L means the domino has been pushed to the left. R means the domino has been pushed to the right. All elements to the left  of an L get pushed to the left and all elements to the right of an R get pushed to the right. If a domino is pushed in both directions simultaneously, it stays up.
# Given the starting state array, return the updated array representing the final state of the dominos. All dominos should be L, R or . if it stays standing upright.

# Examples
# [., L, ., R, .] -> [L, L, ., R, R]
# [., R, ., ., L, .] -> [., R, R, L, L, .]
# [., R, ., ., ., L, .] -> [., R, R, .,  L, L, .]
# [., R, R, ., L, L, .]
 
#  [., ., ., R, , ., ., .] -> [., ., ., R, R, R, R, R]
#  [., ., ., R, L, ., ., .] -> [., ., ., R, L, ., ., .]
#  [R]-> [R]
def dominos(initial_state):
    input = initial_state
    output = ['.'] * len(input)
    stable = False

    while not stable:
        stable = True
        for i in range(len(input)):
            prev = input[i-1] if i > 0 else '.'
            cur = input[i]
            next = input[i+1] if i < (len(input) - 1) else '.'
            if prev == 'R' and next == 'L' or cur != '.':
                output[i] = cur
            elif prev == 'R':
                output[i] = 'R'
                stable = False
            elif next == 'L':
                output[i] = 'L'
                stable = False
        input = output

    return output

dom = ['.', 'R', '.', '.', 'L', '.']
print(dom, '->', dominos(dom))
dom = ['.', 'L', '.', 'R', '.']
print(dom, '->', dominos(dom))
dom = ['.', 'R', '.', '.', '.', 'L', '.']
print(dom, '->', dominos(dom))
dom = ['R']
print(dom, '->', dominos(dom))
