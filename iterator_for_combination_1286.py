'''
1286. Iterator for Combination
Medium

Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false

https://leetcode.com/problems/iterator-for-combination/
'''
from itertools import combinations
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combs = ["".join(c) for c in combinations(characters, combinationLength)]

    def next(self) -> str:
        return self.combs.pop(0)

    def hasNext(self) -> bool:
        return bool(self.combs)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
