'''
98. Validate Binary Search Tree
Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true

https://leetcode.com/problems/validate-binary-search-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTRecc(root, float('-inf'), float('inf'))
    
    def isValidBSTRecc(self, node, minVal, maxVal):
        if not node:
            return True
        if node.val > minVal and node.val < maxVal and self.isValidBSTRecc(node.left, minVal, node.val) and self.isValidBSTRecc(node.right, node.val, maxVal):
            return True
        else:
            return False
