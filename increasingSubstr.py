"""  Find the length of the longest strictly increasing substring that ends at position i """
def incrSubstring(case, N, S):
    result = [1]*N
    
    for i in range(1, N):
        if S[i] > S[i-1]:
            result[i] = result[i-1] + 1
    print(f'Case #{case+1}: ' + ' '.join(map(str, result)))




num_cases = int(input())
test_cases = []
for _ in range(num_cases):
    test_cases.append((int(input()), input()))

for i in range(len(test_cases)):
    incrSubstring(i, test_cases[i][0], test_cases[i][1])
    
""" Input: 
2
4
ABBC
6
ABACDA

Output: 
Case #1: 1 2 1 2
Case #2: 1 2 1 2 3 1

"""