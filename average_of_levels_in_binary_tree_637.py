'''
637. Average of Levels in Binary Tree
Easy

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

https://leetcode.com/problems/average-of-levels-in-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        retVal, sumVal = [], 0
        currQ = [root]
        while currQ:
            currlen = totlen = len(currQ)
            while currlen:
                temp = currQ.pop(0)
                sumVal += temp.val
                if temp.left:
                    currQ.append(temp.left)
                if temp.right:
                    currQ.append(temp.right)
                currlen -=1
            retVal.append(sumVal/totlen)
            sumVal = 0
        return retVal
