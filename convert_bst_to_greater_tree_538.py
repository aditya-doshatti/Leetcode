'''
538. Convert BST to Greater Tree
Medium

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

 

Example 1:


Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

https://leetcode.com/problems/convert-bst-to-greater-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sumVal = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.convertBST(root.right)
            self.sumVal += root.val
            root.val = self.sumVal
            self.convertBST(root.left)
        return root
        
        # retVal = []
        # def preorder(node):
        #     if not node:
        #         return
        #     retVal.append(node.val)
        #     preorder(node.left)
        #     preorder(node.right)
        
        # def update(node, retVal):
        #     if not node:
        #         return
        #     node.val = sum(retVal[retVal.index(node.val):])
        #     update(node.left, retVal)
        #     update(node.right, retVal)
        
        # preorder(root)
        # retVal.sort()
        # update(root, retVal)
        # return root
