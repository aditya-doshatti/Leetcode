'''
545. Boundary of Binary Tree

Medium

The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:

The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
If a node in the left boundary and has a left child, then the left child is in the left boundary.
If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
The leftmost leaf is not in the left boundary.
The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.

Example 1:


Input: root = [1,null,2,3,4]
Output: [1,3,4,2]
Explanation:
- The left boundary is empty because the root does not have a left child.
- The right boundary follows the path starting from the root's right child 2 -> 4.
  4 is a leaf, so the right boundary is [2].
- The leaves from left to right are [3,4].
Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].
https://leetcode.com/problems/boundary-of-binary-tree/description/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def leftdfs(node):
            if node:
                if node.left is None and node.right is None:
                    return []
                else:
                    if node.left:
                        return [node.val] + leftdfs(node.left)
                    else:
                        return [node.val] + leftdfs(node.right)                
            else:
                return []
        
        def findLeaves(node):
            if node:
                if node.right is None and node.left is None:
                    return [node.val]
                else:
                    return findLeaves(node.left) + findLeaves(node.right)
            else:
                return []
        
        def rightdfs(node):
            if node:
                if node.left is None and node.right is None:
                    return []
                else:
                    if node.right:
                        return rightdfs(node.right) + [node.val]
                    else:
                        return rightdfs(node.left) + [node.val]
            else:
                return []
        leftandleavesandright = [root.val] + leftdfs(root.left) + findLeaves(root.left) + findLeaves(root.right) + rightdfs(root.right)
        return(leftandleavesandright)
        '''
        Wrong answer 40/116
        q ,curr, levels, level = [root], [root.val], defaultdict(list), 0
        while q:
            i = len(q)
            a = copy.deepcopy(curr)
            levels[level].append(a)
            while i:
                node = q.pop(0)
                curr.pop(0)
                if node.left:
                    q.append(node.left)
                    curr.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    curr.append(node.right.val)
                i -= 1
            level += 1
        retVal = []
        print(levels)
        for i in range(2):
            for l in range(len(levels.keys()) - 1):
                # print(len(levels[l][0]) > 1)
                if i != 0 and len(levels[l][0]) > 1:
                    retVal.append(levels[len(levels.keys()) -l - 1][0][-1])
                elif i == 0:
                    retVal.append(levels[l][0][0])
        if len(retVal) % 2:
            mid = len(retVal) // 2 + 1
        else:
            mid = len(retVal) // 2
        retVal[mid:mid] = levels[len(levels.keys()) - 1][0]
        return retVal
        '''
