'''
1022. Sum of Root To Leaf Binary Numbers
Easy

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

 

Example 1:



Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        retVal = 0
        def preOrder(node, curr):
            if not node:
                return 
            curr = curr*2 + node.val
            if not node.left and not node.right:
                nonlocal retVal
                retVal += curr
            preOrder(node.left, curr)
            preOrder(node.right, curr)
        preOrder(root, 0)
        return retVal
