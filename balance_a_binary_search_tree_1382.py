'''
1382. Balance a Binary Search Tree

Medium

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

https://leetcode.com/problems/balance-a-binary-search-tree/description
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sortedList = []
        def preorder(node):
            if node:
                preorder(node.left)
                sortedList.append(node.val)
                preorder(node.right)
        
        def generateTree(shortedList):
            # print(shortedList)
            if not len(shortedList):
                return None
            i, j = 0, len(shortedList)
            if i != j:
                mid = (i + j)//2
                # print(i, j, mid)
                if mid < 0:
                    mid = 0
                node = TreeNode()
                node.left = generateTree(shortedList[:mid])
                node.val =  shortedList[mid]
                node.right = generateTree(shortedList[mid + 1:])
                return node
            return None
        preorder(root)
        # print(sortedList)
        return generateTree(sortedList)
