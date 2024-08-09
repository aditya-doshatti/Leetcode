'''
257. Binary Tree Paths

Easy

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

https://leetcode.com/problems/binary-tree-paths/description/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        retVal = []
        def helper(node, curr):
            if node and not node.left and not node.right:
                retVal.append(curr + str(node.val))
            else:
                curr += str(node.val)
                if node.left:
                    helper(node.left, curr + "->")
                if node.right:
                    helper(node.right, curr + "->")
        if root:
            helper(root, "")
        return retVal
