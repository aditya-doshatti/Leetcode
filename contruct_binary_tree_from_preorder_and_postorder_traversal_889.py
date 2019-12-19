'''
889. Construct Binary Tree from Preorder and Postorder Traversal
Medium

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    preIndx = 0
    postIndx = 0
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not (pre and post):
            return None
        t = TreeNode(pre[self.preIndx])
        if len(pre)==1 or len(post)==1:
            return t
        self.preIndx +=1
        if t.val != post[self.postIndx]:
            t.left = self.constructFromPrePost(pre, post)
        if t.val != post[self.postIndx]:
            t.right = self.constructFromPrePost(pre, post)
        self.postIndx +=1
        return t
