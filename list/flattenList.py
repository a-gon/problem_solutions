'''
    In this problem each linked list node has 3 properties:
    value: Int
    next: Node?
    down: Node?
down is another linked list. We want to flatten this linked list such that all nodes only have nexts and no downs.

1 -> 6
2 -> 8
5 -> 7
In this example:
1.next == 6, 1.down == 2, 2.down == 5
Output:
1 -> 2 -> 8 -> 5 -> 7 -> 6
  
'''
class Node:
    def __init__(self, value = 0, next = None, down = None):
        self.value = value
        self.next = next
        self.down = down

def arrayify(head):
    result = []
    cur = head
    while cur:
        result.append(cur.value)
        cur = cur.next
    return result

def flattenLList(head):
    if not head:
        return
    cur = head
    while cur:
        if cur.down:
            next_nodes = cur.next
            cur.next = flattenLList(cur.down)   
            cur.down = None
            while cur and cur.next:    
                cur = cur.next  
            cur.next = next_nodes
     
        cur = cur.next                

    return head   

list1 = Node(1, Node(2), Node(5, None, Node(7)))
list2 = Node(1, Node(6, Node(7, Node(8), Node(5))))

print(arrayify(flattenLList(list1)), 'expect: [1, 5, 7, 2]')
print(arrayify(flattenLList(list2)), 'expect: [1, 6, 7, 5, 8]')