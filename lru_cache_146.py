'''
146. LRU Cache
Medium

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

https://leetcode.com/problems/lru-cache/
'''
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.begin = Node("dummy", "begin")
        self.end = Node("dummy", "end")
        self.begin.next = self.end
        self.end.prev = self.begin
        self.capacity = capacity
        self.used = 0
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map:
            curr = self.map[key]
            tempPrev = curr.prev
            tempPrev.next = curr.next
            curr.next.prev = tempPrev
            tempNext = self.begin.next
            self.begin.next = curr
            curr.prev = self.begin
            curr.next = tempNext
            curr.next.prev = curr 
            return curr.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            curr = self.map[key]
            tempPrev = curr.prev
            tempPrev.next = curr.next
            curr.next.prev = tempPrev
            tempNext = self.begin.next
            self.begin.next = curr
            curr.prev = self.begin
            curr.next = tempNext
            curr.next.prev = curr
            curr.value = value
            return
        if self.used >= self.capacity:
            tempEnd = self.end.prev
            self.end.prev = tempEnd.prev
            self.end.prev.next = self.end
            tempEnd.next = tempEnd.prev = None
            del self.map[tempEnd.key]
            self.used -= 1
        curr = Node(key, value)
        tempNext = self.begin.next
        curr.prev = self.begin
        curr.next = tempNext
        tempNext.prev = curr
        self.begin.next = curr
        self.used += 1
        self.map[key] = curr
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
