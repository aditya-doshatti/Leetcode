'''
872. Leaf-Similar Trees
Easy

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

https://leetcode.com/problems/leaf-similar-trees/
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        lst1, lst2 = [], []
        self.getList(root1, lst1)
        self.getList(root2, lst2)
        # if len(lst1) == len(lst2):
        #     for i in range(len(lst1)):
        #         if lst1[i] != lst2[i]:
        #             return False
        #     return True
        # else:
        #     return False
        if lst1 == lst2:
            return True
        return False
        
    def getList(self, root, lst):
        if(root.left == None and root.right == None):
            lst.append(root.val)
            return
        if (root.left):
            self.getList(root.left, lst)
        if (root.right):
            self.getList(root.right, lst)
        
