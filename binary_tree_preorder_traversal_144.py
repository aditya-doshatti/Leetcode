'''
144. Binary Tree Preorder Traversal
Medium

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?

https://leetcode.com/problems/binary-tree-preorder-traversal/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        lst, retVal = [root], []
        while lst:
            k = lst.pop(0)
            if k:
                retVal.append(k.val)
                if k.right:
                    lst = [k.right] + lst
                if k.left:
                    lst = [k.left] + lst
        return retVal
