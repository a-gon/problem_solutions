from list_class import ListNode

def getDecimalValue(self, head: ListNode) -> int:
    result = 0
    while head:
        result = (result << 1) | head.val
        
        head = head.next
        
    return result




