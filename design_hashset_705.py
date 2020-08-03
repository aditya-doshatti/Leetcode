'''
705. Design HashSet
Easy

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

https://leetcode.com/problems/design-hashset/
'''
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [[] for i in range(1000)]
    
    def hash(self, key):
        return key % 1000

    def add(self, key: int) -> None:
        hashKey = self.hash(key)
        if not self.contains(key):
            self.arr[hashKey].append(key)

    def remove(self, key: int) -> None:
        hashKey = self.hash(key)
        if self.contains(key):
            self.arr[hashKey].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashKey = self.hash(key)
        return key in self.arr[hashKey]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
