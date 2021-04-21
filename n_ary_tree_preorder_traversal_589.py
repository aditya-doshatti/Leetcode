'''
589. N-ary Tree Preorder Traversal
Easy

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

https://leetcode.com/problems/n-ary-tree-preorder-traversal/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.retVal = []
        def helper(root):
            if root:
                self.retVal.append(root.val)
                for child in root.children:
                    helper(child)
        helper(root)
        return self.retVal
