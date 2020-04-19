'''
988. Smallest String Starting From Leaf
Medium

Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)

Example 1:

Input: [0,1,2,3,4,3,4]
Output: "dba"

https://leetcode.com/problems/smallest-string-starting-from-leaf/
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        retVal = []
        def helper(node, temp):
            if node:
                if not node.left and not node.right:
                    retVal.append(chr(node.val + 97)+temp)
                    return
                if node.left:
                    helper(node.left, chr(node.val + 97)+temp)
                if node.right:
                    helper(node.right, chr(node.val + 97)+temp)
            return
        temp = ''
        helper(root, temp)
        return sorted(retVal)[0]
