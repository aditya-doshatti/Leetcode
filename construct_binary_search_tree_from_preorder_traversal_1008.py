'''
1008. Construct Binary Search Tree from Preorder Traversal
Medium

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            node = root
            while True:
                if preorder[i] <= node.val:
                    if node.left:
                        node = node.left
                    else:
                        node.left = TreeNode(preorder[i])
                        break
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = TreeNode(preorder[i])
                        break
        return root
