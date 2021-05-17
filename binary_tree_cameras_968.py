'''
968. Binary Tree Cameras
Hard

Given a binary tree, we install cameras on the nodes of the tree. 

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.

 

Example 1:


Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

https://leetcode.com/problems/binary-tree-cameras/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.retVal = 0
        covered = {None}

        def dfs(node, parent = None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (parent is None and node not in covered or
                        node.left not in covered or node.right not in covered):
                    self.retVal += 1
                    covered.update({node, parent, node.left, node.right})
        dfs(root)
        return self.retVal
