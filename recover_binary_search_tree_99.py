'''
99. Recover Binary Search Tree
Hard

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2

https://leetcode.com/problems/recover-binary-search-tree/
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.prev = None
        self.swaplist = []
        
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.traversal(root)
        if len(self.swaplist) == 1:
            self.swap(self.swaplist[0][0], self.swaplist[0][1])
        elif len(self.swaplist) == 2:
            self.swap(self.swaplist[0][0], self.swaplist[1][1])

    def traversal(self, root):
        if root == None:
            return
        self.traversal(root.left)
        if self.prev and self.prev.val > root.val:
            self.swaplist.append((self.prev, root))
        self.prev = root
        self.traversal(root.right)
            
        
    def swap(self, val1, val2):
        val1.val, val2.val = val2.val, val1.val
