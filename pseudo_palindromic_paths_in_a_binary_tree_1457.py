'''
1457. Pseudo-Palindromic Paths in a Binary Tree
Medium

Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

 

Example 1:



Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def isPseudoPalindromic():
            oddCnt = 0
            for i in range(10):
                if cnt[i] % 2 == 1:
                    oddCnt += 1
            return oddCnt <= 1
        
        def helper(root):
            nonlocal retVal
            if root == None:
                return
            cnt[root.val] += 1
            if root.left == None and root.right == None: # Is leaf node
                if isPseudoPalindromic():
                    retVal += 1
                cnt[root.val] -= 1
                return
            helper(root.left)
            helper(root.right)
            cnt[root.val] -= 1
        
        cnt = [0] * 10
        retVal = 0
        helper(root)
        return retVal
