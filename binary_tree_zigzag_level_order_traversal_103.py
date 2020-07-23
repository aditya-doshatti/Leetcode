'''
103. Binary Tree Zigzag Level Order Traversal
Medium

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q, next_q, retVal, this_level, flag = [root], [], [], [], 0
        while q:
            node = q.pop(0)
            this_level.append(node.val)
            if node.left:
                next_q.append(node.left)
            if node.right:
                next_q.append(node.right)
            if not q:
                if flag:
                    flag = 0
                    retVal.append(this_level[::-1])
                else:
                    flag = 1
                    retVal.append(this_level)
                this_level = []
                q = next_q
                next_q = []
        return retVal
