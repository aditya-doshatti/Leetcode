'''
285. Inorder Successor in BST

Medium

Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

https://leetcode.com/problems/inorder-successor-in-bst/description/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        retVal = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                retVal = root
                root = root.left
        return retVal
        '''
        retNode, matched = None, False
        def helper(Node, p):
            nonlocal retNode
            if Node == None or retNode != None:
                return None
            helper(Node.left, p)
            # print("before", p)
            nonlocal matched
            if matched and retNode == None:
                # print("here")
                retNode = Node
            elif Node.val == p.val:
                matched = True
            
            # print("after", p, Node.val)
            helper(Node.right, p)
        helper(root, p)
        return retNode
        '''
