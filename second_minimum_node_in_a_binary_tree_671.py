'''
671. Second Minimum Node In a Binary Tree

Easy

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.


Example 1:


Input: root = [2,2,5,null,null,5,7]
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        tree = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            tree.append(node.val)
            inorder(node.right)
        inorder(root)
        setVal = set(tree)
        if len(setVal) < 2:
            return -1
        sorted_list = sorted(setVal)
        return sorted_list[1]
        '''
        retVal = -1
        def helper(node):
            nonlocal retVal
            if node.right:
                if node.val != node.left.val:
                    retVal = node.val
                    helper(node.left)
                if node.val != node.right.val:
                    retVal = node.val
                    helper(node.right)
            return
        helper(root)
        return retVal
        '''
