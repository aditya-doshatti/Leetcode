'''
2196. Create Binary Tree From Descriptions

Medium

You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.

 

Example 1:


Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.

https://leetcode.com/problems/create-binary-tree-from-descriptions/description
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hasParent, noParent, dic = set(), set(), {}
        for desc in descriptions:
            # print(dic, desc)
            if not desc[0] in dic:
                dic[desc[0]] = TreeNode(desc[0])
            if not desc[1] in dic:
                dic[desc[1]] = TreeNode(desc[1])
            node = dic[desc[0]]
            if desc[2]:
                node.left = dic[desc[1]]
            else:
                node.right = dic[desc[1]]
            if desc[1] in noParent:
                noParent.remove(desc[1])
            hasParent.add(desc[1])
            if desc[0] not in hasParent:
                noParent.add(desc[0])
        return dic[list(noParent)[0]]
