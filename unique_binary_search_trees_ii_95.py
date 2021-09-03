'''
95. Unique Binary Search Trees II
Medium

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

https://leetcode.com/problems/unique-binary-search-trees-ii/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(1)]
        dp = {}
        def helper(l, r):
            nonlocal dp
            if (l,r) in dp:
                return dp[(l,r)]
            if l > r:
                return [None]
            trees = []
            for root in range(l, r+1):
                for left in helper(l, root-1):
                    for right in helper(root+1, r):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)
            dp[(l,r)] = trees
            return trees
        return helper(1, n) 
