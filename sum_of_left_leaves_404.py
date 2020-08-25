'''
404. Sum of Left Leaves
Easy

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

https://leetcode.com/problems/sum-of-left-leaves/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        retVal = {'val': 0}
        
        def helper(node):
            if not node.left and not node.right:
                retVal['val'] += node.val
        if not root:
            return 0
        lst = [root]
        while lst:
            node = lst.pop()
            if node.left:
                helper(node.left)
                lst.append(node.left)
            if node.right:
                lst.append(node.right)
        return retVal['val']
