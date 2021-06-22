def minOperations(n: int) -> int:
        arr = [(2*i)+1 for i in range(n)]
        print(arr)
        result = 0
        x = 0
        y = len(arr)-1
        # print(abs(n-arr[0]) + abs(n-arr[-1]))
        while arr.count(arr[0]) != len(arr):
            arr[x] += 1
            arr[y] -= 1
            x = arr.index(min(arr))
            y = arr.index(max(arr))
            result += 1
        # print(f'final array: {arr}')
        calc = n*n // 4
        
        return result, calc
        


print(minOperations(7))
print(minOperations(6))

print(minOperations(15))
print(minOperations(3))
print(minOperations(20))
