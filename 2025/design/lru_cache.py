from collections import deque


class LRUCacheBigON:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move recently used key to the end
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.queue.remove(key)  # Remove from old position
        elif len(self.cache) >= self.capacity:
            # Remove least recently used (LRU) key
            lru_key = self.queue.popleft()
            del self.cache[lru_key]

        # Insert new key-value pair
        self.cache[key] = value
        self.queue.append(key)


class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.prev, self.next = None, None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert(self, node):
        prev, nxt = self.right.prev, self.right
        nxt.prev = node
        prev.next = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)

        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.capacity:
            node = self.left.next
            self._remove(node)
            del self.cache[node.key]