""" 
Given an integer n (in base 10) and a base k, 
return the sum of the digits of n after converting n from base 10 to base k. 
"""
def sumBase(n: int, k: int) -> int:
    result = 0
    while n > 0:
        result += n % k     # sum remainder
        n //= k             # get quotient
    return result   


n_k = [(34, 6), (10, 10), (42, 2)]
print(f'{[sumBase(n, k) for n, k in n_k]}')
# output: [9, 1, 3]
