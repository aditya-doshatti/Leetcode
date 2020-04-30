'''
124. Binary Tree Maximum Path Sum
Hard

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        retlist = []
        def helper(node):
            if not node:
                return 0
            else:
                l = helper(node.left)
                r = helper(node.right)
                intermidiate = max(l+node.val, r+node.val, node.val)
                heapq.heappush(retlist, -1 * intermidiate)
                heapq.heappush(retlist, -1 * (l+node.val+r))
                return intermidiate
        helper(root)
        return heapq.heappop(retlist) * -1
