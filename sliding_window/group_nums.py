'''// Given an array of 0s and 1s, group all 0s on one side and 1s on the other side using the minimum number of moves possible. A "move" is a swap between any adjacent positions. 
// return num of swaps

// Examples
// [0, 1] => 0, no swaps are needed since they are already grouped.
// [0, 1, 0] => 1, swap 1 with either 0 to group them.
// [1, 0, 1, 1, 0] => 2, swap 0 with 1 then swap it again with the next 1.
'''


def numSwaps(input):
    ''' this approach works not only for 1s and 0s, will work to group any number combinations, ex: [1,2,3,1,2,3,3] '''
    visited = [False] * 2
    minSwaps = 0
    for i in range(len(input)):
        # if element is seen first time
        print('input[i] = ', input[i])
        if not visited[input[i]]:
            visited[input[i]] = True
            print("visited:", visited)


            count = 0
            
            for j in range(i+1, len(input)):
                # increment if cur element hasn't been visited yet (if visited it means it is in its correct place)
                print("input[j]=", input[j])
                if not visited[input[j]]:
                    count += 1
                    print("count:", count)
                # if current element's partner is found
                elif input[i] == input[j]:
                    minSwaps += count
                    print('minSwaps = ', minSwaps)
                    
    return minSwaps
    


print(numSwaps([1, 0, 1]), "expected 1\n")
print(numSwaps([1, 1, 1, 1, 0]), "expected 0\n")
print(numSwaps([1, 1, 0, 1, 0]), "expected 1\n")
print(numSwaps([0, 0, 1, 1, 0]), "expected 2\n")
print(numSwaps([1, 1, 1, 1, 1]), "expected 0\n")
print(numSwaps([0, 1, 1, 0, 0, 1, 0, 1]), "expected 3")