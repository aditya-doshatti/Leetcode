'''
662. Maximum Width of Binary Tree
Medium

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

https://leetcode.com/problems/maximum-width-of-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: 
            return 0
        retVal = 0
        queue = [(root, 0)]
        while queue: 
            retVal = max(retVal, queue[-1][1] - queue[0][1] + 1)
            temp = []
            for node, i in queue: 
                if node.left: temp.append((node.left, 2*i))
                if node.right: temp.append((node.right, 2*i+1))
            queue = temp
        return retVal 
