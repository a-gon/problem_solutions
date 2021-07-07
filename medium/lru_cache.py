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



