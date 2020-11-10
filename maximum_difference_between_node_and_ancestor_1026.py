'''
1026. Maximum Difference Between Node and Ancestor
Medium

Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.

 

Example 1:


Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        def helper(root, temp_max, temp_min):
            if not root:
                return temp_max - temp_min
            temp_max = max(temp_max, root.val)
            temp_min = min(temp_min, root.val)
            l_val = helper(root.left, temp_max, temp_min)
            r_val = helper(root.right, temp_max, temp_min)
            return max(l_val, r_val)
        return helper(root, root.val, root.val)
