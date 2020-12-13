'''
865. Smallest Subtree with all the Deepest Nodes
Medium

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is tree consisting of that node, plus the set of all descendants of that node.

Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.

https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        rows = []
        rows.append([(root, None)])
        k = 0
        while k != -1:
            tot = len(rows[k])
            if tot == 0:
                k = -1
            else:
                rows.append([])
                k += 1
            i = 0
            while i < tot:
                node = rows[k-1][i][0]
                if node.left:
                    rows[k].append((node.left, node))
                if node.right:
                    rows[k].append((node.right, node))
                i += 1
        l = len(rows)-2
        if len(rows[l]) ==1 :
            return rows[l][0][0]
        par = set()
        for val in rows[l]:
            par.add(val[0])
        while l:
            #print(par)
            for val in rows[l]:
                if val[0] in par:
                    par.add(val[1])
                    par.remove(val[0])
            if len(par) != 1:
                l -= 1
            else:
                return list(par)[0]
        return root
