from list_class import ListNode
""" Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions. """

def partition(head: ListNode, x: int) -> ListNode:
    lt = lt_head = ListNode(-101)
    gte = gte_head = ListNode(101)
    cur = head
    
    while cur:
        if cur.val < x:
            lt.next = cur
            lt = lt.next
        else:
            gte.next = cur
            gte = gte.next
            
        cur = cur.next
        
    gte.next = None    
    lt.next = gte_head.next
    
    return lt_head.next

""" Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5] """

vals = [1,4,3,2,5,2]
head = ln = ListNode(vals.pop(0))
while vals:
    ln.next = ListNode(vals.pop(0))
    ln = ln.next

part = partition(head, 3)
result = []
while part:
    result.append(part.val)
    part = part.next

print(f'After partition: {result}')


