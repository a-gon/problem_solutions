def sumDigits(num):
    sum = 0
    while num:
        sum += num % 10
        num //= 10
    
    return sum



input = 7119
print(f'Sum of digits: {sumDigits(input)}')

