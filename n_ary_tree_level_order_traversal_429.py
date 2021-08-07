'''
429. N-ary Tree Level Order Traversal
Medium

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

https://leetcode.com/problems/n-ary-tree-level-order-traversal/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        retVal = []
        if not root:
            return retVal
        retVal.append([])
        currLevel, nxtLevel, i = [root], [], 0
        while currLevel:
            node = currLevel.pop(0)
            retVal[i].append(node.val)
            nxtLevel += node.children
            if len(currLevel) == 0:
                currLevel = nxtLevel
                nxtLevel = []
                retVal.append([])
                i += 1
        return retVal[:-1]
