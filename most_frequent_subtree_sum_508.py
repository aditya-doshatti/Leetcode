'''
508. Most Frequent Subtree Sum
Solved
Medium
Topics
Companies
Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

 

Example 1:


Input: root = [5,2,-3]
Output: [2,-3,4]

https://leetcode.com/problems/most-frequent-subtree-sum/description/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        dic_sums = defaultdict(int)
    
        def helper(node, curr_sum):
            if node:
                sumr, suml = 0, 0
                if node.left:
                    suml = helper(node.left, curr_sum)
                if node.right:
                    sumr = helper(node.right, curr_sum)
                curr_sum += node.val + sumr + suml
            dic_sums[curr_sum] += 1
            return curr_sum
        helper(root, 0)
        
        maxVal = float('-inf')
        # print(dic_sums)
        
        for k, v in dic_sums.items():
            if v > maxVal:
                retVal = []
                retVal.append(k)
                maxVal = v
            elif v == maxVal:
                retVal.append(k)
        return retVal

