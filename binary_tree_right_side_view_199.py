'''
199. Binary Tree Right Side View
Medium

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

https://leetcode.com/problems/binary-tree-right-side-view/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import OrderedDict 
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        retVal = []
        tree = OrderedDict()
        tree.setdefault(0, [])
        tree[0].append(root)
        nodeList = [(root,0)]
        while nodeList:
            # print(nodeList)
            val, key = nodeList.pop(0)
            if val.left:
                tree.setdefault(key+1, [])
                tree[key+1].append(val.left)
                nodeList.append((val.left, key+1))
            if val.right:
                tree.setdefault(key+1, [])
                tree[key+1].append(val.right)
                nodeList.append((val.right, key+1))    
        # print(tree)
        for key in tree:
            retVal.append(tree[key][-1].val)
        return retVal

