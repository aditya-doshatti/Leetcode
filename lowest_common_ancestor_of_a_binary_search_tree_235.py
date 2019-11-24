'''
235. Lowest Common Ancestor of a Binary Search Tree
Easy

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val == root.val or q.val == root.val:
                return root
            if p.val < q.val:
                if (p.val < root.val and q.val > root.val):
                    return root
            else:
                if (q.val < root.val and p.val > root.val):
                    return root
            if p.val > root.val:
                root = root.right
            else:
                root = root.left
