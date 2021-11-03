'''
129. Sum Root to Leaf Numbers
Medium

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

https://leetcode.com/problems/sum-root-to-leaf-numbers/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, path_sum):
            if not root:
                return 0
            if (root.left is None) and (root.right is None):
                return path_sum*10 + root.val
            return dfs(root.left, path_sum*10 + root.val) + \
        dfs(root.right, path_sum*10 + root.val)
        return dfs(root, 0)
    '''
        lst, retVal, retlist = "",0, []
        if root != None:
            self.helper(root, lst,retlist)
        for i in retlist:
            retVal += int(i)
        return retVal
    
    
    def helper(self, root, lst, retVal):
        if root!=None and root.left == None and root.right == None:
            lst+=str(root.val)
            retVal.append(lst)
        elif root!=None:
            lst+= str(root.val)
            self.helper(root.left, lst, retVal)
            self.helper(root.right, lst, retVal)
    '''
