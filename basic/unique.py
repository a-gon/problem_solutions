# Number of unique elements [1,1,2,3] -> 3

# Most frequent element in array

# Least frequent element in array

# Number of elements with exactly 2 occurrences ([1, 2, 1, 3, 2, 4] returns 2)

'''
initialize dictionary
iterate through the array
keep element counts in a map
counts = {}
increment the element count on first encounter
return the length on map

'''



def numUniqueElems(input):
    
    return len(set(input))



'''
initialize dictionary
initialize a maxOccurences at 1
initialize a mostFrequent 

iterate over array and add/increment values in dictionary

maxOccurences would be set to the max of value at given element or maxOccurences
if the value of element is equal to maxOccurences, then mostFrequent equals element

return mostFrequent
'''

def mostFreqElem(input):
    counts = {}
    maxOccurences = 0
    #mostFrequent
    
    for elem in input:
        
        if elem not in counts:
            counts[elem] = 0
        
        counts[elem] += 1
            
        if counts[elem] > maxOccurences:
            maxOccurences = counts[elem]
            mostFrequent = elem
            
    return mostFrequent
        

def leastFreqElem(input):
    counts = {}
    minOccurences = len(input)
    # leastFrequent
    for elem in input:
        
        if elem not in counts:
            counts[elem] = 0
        
        counts[elem] += 1
        
    for k, v in counts.items():
        if v < minOccurences:
            minOccurences = v
            leastFrequent = k

            
    return leastFrequent

    
    
    

test = [3,2,3, 3,2,2, 1]
print(leastFreqElem(test), 'expect 1')