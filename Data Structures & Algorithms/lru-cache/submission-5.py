class Node:
    def __init__(self, key, val): 
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity 
        self.head = None 
        self.tail = None
    
    def insert(self, node):
        node.prev = self.tail 
        node.next = None 
        if self.tail:
            self.tail.next = node 
        else: 
            self.head = node 
        self.tail = node

    def remove(self, node):
        if node.prev: 
            node.prev.next = node.next 
        else:
            self.head = node.next
        if node.next: 
            node.next.prev = node.prev
        else: 
            self.tail = node.prev
        node.prev = node.next = None 

    def get(self, key: int) -> int:
        if key in self.cache: 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.head
            self.remove(lru)
            del self.cache[lru.key]


        

            
        

            
        
        
