def validateStackSequences(pushed, popped) -> bool:
    '''
    cur_stack: [123]  cur_popped:[45]
    popped_seq = [4,5,3,2,1]
                        i
    pushed_seq = [1,2,3,4,5]
                            i
    
    
    popped = popped_seq -> True
    ---
    input_stack: [12345 _ ] (nothing left in input)
    stack:[1,2], popped:435 curStack[-1] != popped_input[0] -> False
    popped_input: [12]
    
    '''
    
    
    if len(pushed) != len(popped):
        return False
    Len = len(pushed)
    curStack = []
    curPopped = []
#         keep appending to curStack and checking if elem == popped[0]
    popped_i = 0
    pushed_i = 0
    while pushed_i < Len or popped_i < Len:

        if curStack and curStack[-1] == popped[popped_i]:
            curPopped.append(curStack.pop())
            popped_i += 1
        else:
            if pushed_i == Len:
                break
            curStack.append(pushed[pushed_i])
            pushed_i += 1
            

            
    return len(curStack) == 0
        

'''
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false

'''
print(validateStackSequences([1,2,3,4,5], [4,5,3,2,1]), 'expect True')
print(validateStackSequences([1,2,3,4,5], [4,3,5,1,2]), 'expect False')




def validateStackSequencesV2(pushed, popped) -> bool:

    if len(pushed) != len(popped):
        return False
    Len = len(pushed)
    curStack = []
#         keep appending to curStack and checking if elem == popped[0]
    popped_i = 0
    pushed_i = 0
    while pushed_i < Len:
        curStack.append(pushed[pushed_i])
        pushed_i += 1
        while curStack and curStack[-1] == popped[popped_i]:
            curStack.pop()
            popped_i += 1
            
            
    return popped_i == len(popped)

