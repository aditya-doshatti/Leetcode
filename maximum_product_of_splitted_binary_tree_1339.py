# Definition for a binary tree node.
'''
1339. Maximum Product of Splitted Binary Tree
Medium

Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sumVal = 0
        lst = [root]
        while lst:
            node = lst.pop(0)
            sumVal += node.val
            if node.left:
                lst.append(node.left)
            if node.right:
                lst.append(node.right)
        sumVals = []
        def subTreeSum(node):
            # print(sumVals)
            if not node:
                return 0
            lsum, rsum = 0, 0
            if node.left:
                lsum = subTreeSum(node.left)
            if node.right:
                rsum = subTreeSum(node.right)
            # print(node.val, lsum, rsum)
            curVal = node.val + lsum + rsum
            # print(curVal)
            sumVals.append(abs(sumVal-curVal)*curVal)
            return curVal
        subTreeSum(root)
        # print(sumVals)
        return max(sumVals) % (10**9 + 7)
            
