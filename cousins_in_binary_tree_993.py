'''
993. Cousins in Binary Tree
Easy

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false

https://leetcode.com/problems/cousins-in-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        prevlevel, levelParents, curr, vals = [root],  [(root.val, None)], [], set()
        while prevlevel:
            node = prevlevel.pop(0)
            if node.left:
                curr.append(node.left)
                vals.add(node.left.val)
                levelParents.append((node.left.val, node))
            if node.right:
                curr.append(node.right)
                vals.add(node.right.val)
                levelParents.append((node.right.val, node))
            if not prevlevel:
                if x in vals:
                    if y not in vals:
                        return False
                    else:
                        p1 = None
                        while levelParents:
                            n, p = levelParents.pop(0)
                            if n == x or n == y:
                                if p1:
                                    if p != p1:
                                        return True
                                    else:
                                        return False
                                else:
                                    p1 = p
                prevlevel = curr
                curr = []
                levelParents = []
            else:
                continue
        return False
