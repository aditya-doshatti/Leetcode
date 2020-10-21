'''
938. Range Sum of BST
Easy

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

https://leetcode.com/problems/range-sum-of-bst/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.retVal = 0 
        self.helper(root, L, R)
        return self.retVal
    
    def helper(self, node, L, R):
        if node:
            if L <= node.val <= R:
                self.retVal += node.val
            if node.val > L:
                self.helper(node.left, L , R)
            if node.val < R:
                self.helper(node.right, L , R)
