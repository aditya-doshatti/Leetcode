'''
Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 

We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.

Example 1:

Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
Output: true
Explanation: 
The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure). 
Other valid sequences are: 
0 -> 1 -> 1 -> 0 
0 -> 0 -> 0

https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3315/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        temp = []
        node = root
        while node or temp:
            if not node:
                node, arr = temp.pop()
            else:
                if node.val == arr[0]:
                    arr.pop(0)
                    if not arr:
                        if not node.left and not node.right:
                            return True
                        else:
                            node = None
                            continue
                    if node.right and node.right.val == arr[0]:
                        if node.left and node.left.val == arr[0]:
                            temp.append((node.left, arr[::]))
                        node = node.right
                    elif node.left and node.left.val == arr[0]:
                        node = node.left
                    else:
                        node = None
                else:
                    node = None
        return False
