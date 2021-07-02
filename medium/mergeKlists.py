class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next
        
def arrayify(head):
    if not head:
        return None
    output = []
    cur = head
    while cur:
        output.append(cur.value)
        cur = cur.next
    return output
        

def merge2lists(list1, list2):
    if not list1 or not list2:
        return list1 or list2
    head = ListNode(0)
    cur = head
    while list1 and list2:
        if list1.value < list2.value:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
        
    cur.next = list1 or list2
        
    return head.next

# ll1 = ListNode(1, ListNode(2, ListNode(3)))
# ll2 = ListNode(2, ListNode(3, ListNode(4)))
# print(arrayify(merge2lists(ll1, ll2)), 'expected: [1, 2, 2, 3, 3, 4]')

# [ll1    ll2    ll3]
# interval = 1 -> ll1 = merge (ll1, ll2), ll3 = stays
# interval = 2 -> ll1 = merge(ll1, ll3)
# return ll1

def mergeKlists(lists):
    if not lists:
        return None
    interval = 1
    while interval < len(lists):
        for i in range(0, len(lists) - interval, interval * 2):
            lists[i] = merge2lists(lists[i], lists[i+interval])
        interval *= 2
        
    return lists[0]

ll1 = ListNode(1, ListNode(2, ListNode(4)))
ll2 = ListNode(3, ListNode(5, ListNode(6)))
ll3 = ListNode(7, ListNode(8))
print('---Merge K lists---')
print(arrayify(mergeKlists([ll1, ll2, ll3])), 'expected: [1, 2, 3, 4, 5, 6, 7, 8]')



''' 
def mergeKLists(lists):
Given an array of sorted linked lists, merge all of them into one sorted list
1. Brute force O(nlogn) time (because of sorting), O(n) space - size of an array with all inputs
    - iterate over all linked lists and store all the values into an array
    - sort the array
    - create a new linked list and add new nodes with values from the sorted array
2. Compare one by one
    - compare the first node of each list
        - k-1 comparisons for N total nodes in new list >> O(kN) time
    - append the smallest node to the new sorted list
    
    Space: O(N) - N = total nodes to create and return in a new list
    
3. Priority Queue - optimization for (2)

4. Merge lists one by one
    - works like merging 2 lists but repeat with all of the lists k-1 times total
    - O(kN) time, O(1) space
    
5. Merge by Divide and Conquer
    - pair up all the lists (group in pairs)
    - merge each pair into one list
    - repeat the procedure to merge all lists
    Time: O(N log k) - merge two sorted lists is O(n) * log k times (k/2 repeatedly)
    Space: (1)
    
    pseudo-code:
    divide function:
        - for each two lists, 
            - call merge function and store resulting list head
        - resursively call divide funstion on a group of new two lists
    
    merge function:
        while pointers to both lists have not reaches the end,
        connect cur to the smaller of the two nodes
        increment cur and pointers to both lists
        return head of the new merged list
        
        
        
    Example:
    
    [[1,4,5],[1,3,4],[2,6]] => [1,1,2,3,4,4,5,6]
    
    num_lists = 3
    interval = 1
    while interval < num_lists:

        **iter1:
        interval = 1
        for i in range(from 0 to 2, step= 2):
        -lists[0] = merge([1,4,5], [1,3,4]) = [1,1,3,4,4,5]
        -lists[2] = merge([2,6], None) = [2,6]
            
        interval *= 2 = 2
        
        **iter2:
        interval = 2  (< num_lists)
        for i in range(0, 1, 2*2): (do once)
        -lists[0] = merge([1,1,3,4,4,5], [2,6]) = [1,1,2,3,4,4,5,6]
        
        interval *= 2 = 4
        
        4 > 3, so break out of while loop
        
        return lists[0] which is [1,1,2,3,4,4,5,6]
        
        
        
        [[1,4,5],[1,3,4],[2,6],[3,4],[5,7],[5,6]]
            \              \           \      
             \              \           \     
              \              \           \  
          [1,1,3,4,4,5]     [2,3,4,6]     [5,5,6,7]
               \                                    
                \                                  
                 \                                
            [1,1,2,3,4,4,4,5,6]            [5,5,6,7]
                     \                      /
                      \                    /
                       \                  /
                    [1,1,2,3,4,4,4,5,5,6,6,7]
    
    
    
        
        
        
'''