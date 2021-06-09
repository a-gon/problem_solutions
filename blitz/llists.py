class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next
        
def arrayify(head):
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array


# def removeNodes(head, target: int) -> ListNode:
#     """ remove nodes with target value """
#     # recursively:
#     if not head:
#         return None
#     if head.next:
#         head.next = removeNodes(head.next, target)
#     if target == head.value:
#         return head.next
#     return head

def removeNodes(head, target: int) -> ListNode:
    """ remove all nodes with target value (edge case: head.val == target)"""
    # iteratively
    if not head:
        return None
    sentinel = ListNode(0, head)
    cur = sentinel
    while cur.next:
        if cur.next.value == target:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return sentinel.next
    

LL1 = ListNode(4, ListNode(1, ListNode(2, ListNode(1, ListNode(3, ListNode(2, ListNode(2)))))))
assert(arrayify(removeNodes(None, 1))) == []
assert(arrayify(removeNodes(LL1, 1))) == [4, 2, 3, 2, 2], 'failed case 2'
assert(arrayify(removeNodes(LL1, 2))) == [4, 3]
assert(arrayify(removeNodes(LL1, 3))) == [4]
assert(arrayify(removeNodes(LL1, 4))) == []
print('Remove nodes: All tests passed')


def findMiddle(head: ListNode) -> int:
    """Find middle element in list """
    if not head:
        return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value

# Test Cases
LL1 = ListNode(1, ListNode(3, ListNode(5)))
LL2 = ListNode(1, ListNode(3, ListNode(-13, ListNode(-3, ListNode(1)))))
print('Find middle element')
print(findMiddle(None)) # None
print(findMiddle(LL1)) # 3
print(findMiddle(LL2)) # -13
print(findMiddle(ListNode(1))) # 1


def findKthFromLast(head: ListNode, k: int) -> int:
    """ Find kthe element from the end """ 
    if not head:
        return None
    slow = fast = head
    while fast and k > 0:
        fast = fast.next
        k -= 1
    while fast:
        fast = fast.next
        slow = slow.next
    return slow.value if k == 0 else -1   # if k is larger than the len(list), return -1

# Test Cases
LL1 = ListNode(13, ListNode(1, ListNode(5, ListNode(3, ListNode(7, ListNode(10))))))
print('Find kth from end:')
print(findKthFromLast(LL1, 1)) # 10
print(findKthFromLast(LL1, 3)) # 3
print(findKthFromLast(LL1, 6)) # 13
print(findKthFromLast(LL1, 7)) # -1


def reverseLL(head: ListNode) -> ListNode:
    """ Reverse list"""
    if not head:
        return None
    prev = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev

# Test Cases
LL1 = ListNode(13, ListNode(1, ListNode(5, ListNode(3, ListNode(7, ListNode(10))))))
print("Reverse linked list")
print(arrayify(reverseLL(ListNode(1)))) # [1]
print(arrayify(reverseLL(ListNode(1, ListNode(2))))) # [2, 1]
print(arrayify(reverseLL(LL1))) # [10, 7, 3, 5, 1, 13]