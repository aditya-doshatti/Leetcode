'''
145. Binary Tree Postorder Traversal
Easy

Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]

https://leetcode.com/problems/binary-tree-postorder-traversal/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        retVal = []
        def helper(root, retVal):
            if not root:
                return
            helper(root.left, retVal)
            helper(root.right, retVal)
            retVal.append(root.val)
        helper(root, retVal)
        return retVal
