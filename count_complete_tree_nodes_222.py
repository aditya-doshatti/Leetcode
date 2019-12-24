'''
222. Count Complete Tree Nodes
Medium

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

https://leetcode.com/problems/count-complete-tree-nodes/
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dl = []
        count = 0
        if root == None:
            return 0
        else:
            dl.append(root)
        while dl:
            curr = dl.pop()
            count += 1
            if curr.left:
                dl.append(curr.left)
            if curr.right:
                dl.append(curr.right)
        return count
