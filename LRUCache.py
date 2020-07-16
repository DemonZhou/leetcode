class LinkNode():
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = LinkNode()
        self.tail = LinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.cache = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.MoveToNode(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache:
            node = LinkNode(key,value)
            self.cache[key] = node
            self.AddToHead(node)
            self.size += 1
            if self.size > self.capacity:
                tmp = self.RemoveTail()
                self.cache.pop(tmp.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.MoveToNode(node)

    
    def AddToHead(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


    def RemoveTail(self):
        node = self.tail.prev
        node2 = node.prev
        self.tail.prev = node2
        node2.next = self.tail
        return node
    
    def RemoveNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


    def MoveToNode(self,node):
        self.RemoveNode(node)
        self.AddToHead(node)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)