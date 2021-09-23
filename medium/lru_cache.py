class DLLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
    def removeBindings(self):
        # remove node
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def removeTail(self):
        if not self.tail:
            return 
        if self.head == self.tail:
            self.tail = None
            self.head = None
            return
        self.tail = self.tail.prev
        self.tail.next = None


    def setHeadTo(self, node):
        if self.head == node:
            return
        if self.head == None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBindings() # don't forget to reset the node's rev and next
            self.head.prev = node
            node.next = self.head
            self.head = node
            

class LRUCache:
    def __init__(self, maxSize):
        self.curSize = 0
        self.maxSize = maxSize or 1
        self.cache = {}
        self.list = DLL()

    def insertKeyValuePair(self, key, value):
        if key not in self.cache:
            if self.curSize == self.maxSize:
                self.evictLeastRecent() 
            else:
                self.curSize += 1
            self.cache[key] = DLLNode(key, value)
        else:
            self.replaceKey(key, value)
        self.updateMostRecent(self.cache[key])


    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        self.list.setHeadTo(self.cache[key])   # set this node to be new head since it is being retrieved
        return self.cache[key].value


    def getMostRecentKey(self):
        if not self.list:
            return None
        return self.list.head.key

        
    def evictLeastRecent(self):
        keyToRemove = self.list.tail.key
        self.list.removeTail()
        del self.cache[keyToRemove]

    def replaceKey(self, key, value):
        if key not in self.cache:
            raise Exception('The key is not in cache!')
        self.cache[key].value = value

    def updateMostRecent(self, node):
        self.list.setHeadTo(node)



'''
Implement LRU cache using DLL with a sentinel node:
'''
class Node:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
    
class DLList:
    def __init__(self):
        self.sentinel = Node(-2, -2)
        self.sentinel.next = self.sentinel.prev = self.sentinel
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def add(self, node):
        node.next = self.sentinel.next
        node.prev = self.sentinel
        node.next.prev = node
        self.sentinel.next = node
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cacheList = DLList()
        self.cacheMap = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        # print(f'get {key}')
        if key not in self.cacheMap:
            return -1
        curNode = self.cacheMap[key]
        self.cacheList.remove(curNode)   # remove from list
        self.cacheList.add(curNode)      # always add to front

        return curNode.val

    def put(self, key: int, value: int) -> None:
        # print(f'put {key}:{value}')
        nodeToRemove = None
        newNode = Node(key, value)


        if key in self.cacheMap:
            nodeToRemove = self.cacheMap[key]
        elif len(self.cacheMap) == self.capacity:
            nodeToRemove = self.cacheList.sentinel.prev
            # print(f'keyToDel: {nodeToRemove.key}')
            del self.cacheMap[nodeToRemove.key]
        if nodeToRemove:
            self.cacheList.remove(nodeToRemove)
        self.cacheList.add(newNode)                         # add new node to front
        self.cacheMap[key] = newNode

        # print(self.cacheMap)
        # print(f'head: {self.cacheList.sentinel.next.key}, tail: {self.cacheList.sentinel.prev.key}')



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)