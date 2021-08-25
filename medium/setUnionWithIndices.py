"""
Given two arrays oldIDs and newIDs, return an array that meets the following criteria:
- result contains all values from newIDs
- all ids that exist in oldIDs are in the same index as they were in oldIDs

old = [1,2,3]
new = [4,5,6]

output = [4,5,6]


old = [1,2,3]
new = [3,4,5]

output = [x,x,3] [4,5,3] or [5,4,3]
"""



def preserveSpots2(oldIDs, newIDs):    
    n = len(oldIDs)
    result = [None] * n
    newIDsSet = set(newIDs)
    oldIDsSet = set(oldIDs)
    
    fillValues = list(filter(lambda x: (x not in oldIDsSet), newIDs))
    
    for i in range(n):
        if oldIDs[i] in newIDsSet:
            result[i] = oldIDs[i]
            
    for i in range(n):
        if not result[i]:          
            result[i] = fillValues.pop()
            
    return result


print(preserveSpots2([1,2,3], [3,4,5]))   
    
print(preserveSpots2([1, 2, 3], [1, 2, 3]))    




