'''
100. Same Tree
Easy

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

https://leetcode.com/problems/same-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p != None and q != None:
            if p.val == q.val:
                if self.isSameTree(p.left, q.left):
                    if self.isSameTree(p.right, q.right):
                        return True
            else:
                return False
        elif p == q:
            return True
        else:
            return False
