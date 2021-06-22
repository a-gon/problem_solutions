from math import sqrt
def is_prime(n):
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
 
    if (n % 2 == 0 or n % 3 == 0) :
        return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True


def prime(Z):

    root = int(sqrt(Z))
    num1 = root
    num2 = root

    while not is_prime(num1) and not is_prime(num2) or num1==num2:
        if not is_prime(num1):
            num1 -= 1
        if not is_prime(num2):
            num2 -= 1
            

    
    print(num1 * num2)
    print(num1)
    print(num2)


prime(2020)