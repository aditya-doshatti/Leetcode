'''
1373. Maximum Sum BST in Binary Tree
Hard

Given a binary tree root, the task is to return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:



Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.

https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        maxVal = 0
        def isBst(root):
            nonlocal maxVal
            if not root:
                return True, 0
            else:
                flagL , sumL = isBst(root.left)
                flagR , sumR = isBst(root.right)
                if (root.left and root.left.val >= root.val) or (root.right and root.right.val <= root.val) :
                    return False, 0
                if flagL and flagR:
                    sumVal = root.val + sumL + sumR
                    maxVal = max(sumVal, maxVal)
                    return True, sumVal
                else:
                    return False, 0
        isBst(root)
        return max(maxVal, 0)
                    
        # retList = []
        # def inOrder(root, retList):
        #     if not root:
        #         return
        #     inOrder(root.left, retList)
        #     retList.append(root.val)
        #     inOrder(root.right, retList)
        # inOrder(root, retList)
        # i, retVal, temp = 0, 0, 0
        # print(retList)
        # while i < len(retList):
        #     if i == 0:
        #         if retList[i] < retList[i+1]:
        #             temp += retList[i]
        #         else:
        #             retVal = max(retVal, temp)
        #             temp = 0
        #     if i < len(retList)-1:
        #         if retList[i-1] <= retList[i] <= retList[i+1]:
        #             temp += retList[i]
        #         else:
        #             retVal = max(retVal, temp)
        #             temp = 0
        #     if i == len(retList)-1:
        #         if retList[i-1] < retList[i]:
        #             temp += retList[i]
        #         else:
        #             retVal = max(retVal, temp)
        #             temp = 0
        #     i+=1
        # retVal = max(retVal, temp)
        # return retVal
