'''
971. Flip Binary Tree To Match Preorder Traversal
Medium

You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n. You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.

Any node in the binary tree can be flipped by swapping its left and right subtrees. For example, flipping node 1 will have the following effect:


Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.

Return a list of the values of all flipped nodes. You may return the answer in any order. If it is impossible to flip the nodes in the tree to make the pre-order traversal match voyage, return the list [-1].

 

Example 1:


Input: root = [1,2], voyage = [2,1]
Output: [-1]
Explanation: It is impossible to flip the nodes such that the pre-order traversal matches voyage.

https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.retVal = []
        self.cnt = 0
        
        def helper(node):
            if node:
                if node.val != voyage[self.cnt]:
                    self.retVal = [-1]
                    return
                self.cnt +=1 
                if self.cnt < len(voyage) and node.left and node.left.val != voyage[self.cnt]:
                    self.retVal.append(node.val)
                    helper(node.right)
                    helper(node.left)
                else:
                    helper(node.left)
                    helper(node.right)
        helper(root)
        if self.retVal and self.retVal[0] == -1:
            return [-1]
        return self.retVal
