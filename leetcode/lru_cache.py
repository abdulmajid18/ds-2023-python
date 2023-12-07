class LRUCacheNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-value pairs
        self.head = LRUCacheNode(None, None)  # Dummy head node
        self.tail = LRUCacheNode(None, None)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_node_to_end(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move the accessed node to the end (most recently used)
            self._remove_node(node)
            self._add_node_to_end(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If the key already exists, update its value and move it to the end
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_node_to_end(node)
        else:
            if len(self.cache) >= self.capacity:
                # If the cache is full, remove the least recently used node (at the front)
                lru_node = self.head.next
                self._remove_node(lru_node)
                del self.cache[lru_node.key]
            # Add the new key-value pair to the cache and the end of the linked list
            new_node = LRUCacheNode(key, value)
            self.cache[key] = new_node
            self._add_node_to_end(new_node)


# Example usage:
# Initialize the LRU Cache with a capacity of 2
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Output: 1
cache.put(3, 3)  # The cache is full, so remove the least recently used item (key=2)
print(cache.get(2))  # Output: -1 (key 2 is no longer in the cache)
cache.put(4, 4)  # The cache is full, so remove the least recently used item (key=1)
print(cache.get(1))  # Output: -1 (key 1 is no longer in the cache)
print(cache.get(3))  # Output: 3
print(cache.get(4))  # Output: 4
