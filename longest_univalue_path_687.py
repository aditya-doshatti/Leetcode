'''
687. Longest Univalue Path
Easy

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

 

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

https://leetcode.com/problems/longest-univalue-path/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.retVal = 0
        self.postorder(root)
        return self.retVal
        
    def postorder(self, node):
        if not node:
            return 0
        temp_left = self.postorder(node.left)
        temp_right = self.postorder(node.right)
        left, right = 0, 0
        if  node.left and node.left.val == node.val:
            left = temp_left + 1
        if node.right and node.right.val == node.val:
            right = temp_right + 1
        self.retVal = max(self.retVal, left+right)
        return max(left, right)
