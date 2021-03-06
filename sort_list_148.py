'''
148. Sort List
Medium

Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]

https://leetcode.com/problems/sort-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        lst = []
        node =  head
        while node:
            lst.append(node.val)
            node = node.next
        lst.sort()
        node = head
        for n in lst:
            node.val = n
            node = node.next
        return head
