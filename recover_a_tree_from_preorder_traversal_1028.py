'''
1028. Recover a Tree From Preorder Traversal
Hard

We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  (If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.


Example 1:



Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        dic, i, d, temp = defaultdict(list), 0, 0, ''
        while i < len(S):
            if S[i] == '-':
                d +=1
            else:
                temp += S[i]
                if i+1 < len(S) and S[i+1] != '-':
                    i +=1
                    continue
                elif d == 0:
                    newNode = TreeNode(temp)
                    dic[d].append(newNode)
                    temp = ''
                else:
                    val = dic[d-1][-1]
                    newNode = TreeNode(temp)
                    if val.left:
                        val.right = newNode
                    else:
                        val.left = newNode
                    dic[d].append(newNode)
                    d = 0
                    temp = ''
            i+=1
        return dic[0][0]
