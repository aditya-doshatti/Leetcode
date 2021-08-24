'''
653. Two Sum IV - Input is a BST
Easy
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def pushLeft(st, root):
            while root:
                st.append(root)
                root = root.left

        def pushRight(st, root):
            while root:
                st.append(root)
                root = root.right

        def nextLeft(st):
            node = st.pop()
            pushLeft(st, node.right)
            return node.val

        def nextRight(st):
            node = st.pop()
            pushRight(st, node.left)
            return node.val

        leftVals, rightVals = [], []
        pushLeft(leftVals, root)
        pushRight(rightVals, root)

        left, right = nextLeft(leftVals), nextRight(rightVals)
        while left < right:
            if left + right == k: 
                return True
            if left + right < k:
                left = nextLeft(leftVals)
            else:
                right = nextRight(rightVals)
        return False
