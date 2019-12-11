'''
111. Minimum Depth of Binary Tree
Easy

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

https://leetcode.com/problems/minimum-depth-of-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q, retVal = [], 0
        q.append(root)
        while q:
            retVal +=1
            levelSize = len(q)
            while levelSize > 0:
                node = q.pop(0)
                if not node.left and not node.right:
                    return retVal
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                levelSize -= 1
        # 32 ms vs 44 ms
        # if not root:
        #     return 0
        # elif not root.left and not root.right:
        #     return 1
        # else:
        #     left = self.minDepth(root.left)
        #     right =  self.minDepth(root.right)
        #     if min(left, right):
        #         return 1 + min(left, right)
        #     else:
        #         return 1 + max(left, right)
            
