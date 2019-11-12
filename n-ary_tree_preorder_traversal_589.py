'''
589. N-ary Tree Preorder Traversal
Easy

Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:


Return its preorder traversal as: [1,3,5,6,2,4].

Note:
Recursive solution is trivial, could you do it iteratively?

https://leetcode.com/problems/n-ary-tree-preorder-traversal/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        l, retVal = [], []
        l.append(root)
        while len(l):
            k =l.pop(0)
            retVal.append(k.val)
            if k.children:
                l = k.children + l
        return retVal
            
