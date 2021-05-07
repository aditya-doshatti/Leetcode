'''
109. Convert Sorted List to Binary Search Tree
Medium

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

 

Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def helper(beg, end):
            if beg > end: return None
            mid = (beg + end)//2
            left = helper(beg, mid - 1)
            root = TreeNode(self.head.val)
            self.head = self.head.next
            root.left = left
            root.right = helper(mid + 1, end)
            return root
        self.head, tmp, n = head, head, 0
        while tmp:
            tmp = tmp.next
            n += 1
        return helper(0, n-1)
