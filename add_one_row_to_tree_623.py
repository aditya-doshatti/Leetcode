'''
623. Add One Row to Tree
Medium

Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

v = 1

d = 2

Output: 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5  

https://leetcode.com/problems/add-one-row-to-tree/ 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        origRoot = root
        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot
        level = 0
        q = [root]
        while level != d-2:
            i = len(q)
            while i > 0:
                temp = q.pop(0)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                i -=1
            level += 1
        for node in q:
            if node.left:
                templeft = node.left
                node.left = TreeNode(v)
                node.left.left = templeft
            else:
                node.left = TreeNode(v)
            if node.right:
                tempright = node.right
                node.right = TreeNode(v)
                node.right.right = tempright
            else:
                node.right = TreeNode(v)
        return origRoot
