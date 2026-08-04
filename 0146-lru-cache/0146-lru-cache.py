class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        return None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.lru = Node(0,0)
        self.mru = Node(0,0)
        self.lru.next = self.mru
        self.mru.prev = self.lru
        return None

    def remove(self, node):
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left
        return None
    
    def insert(self, node):
        right = self.mru
        left = self.mru.prev
        node.prev = left
        node.next = right
        left.next = node
        right.prev = node
        return None

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
   

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.insert(node)
            self.cache[key] = node
        if len(self.cache) > self.cap :
            node = self.lru.next
            self.remove(node)
            del self.cache[node.key]
        return None



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)