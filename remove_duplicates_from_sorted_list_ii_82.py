'''
82. Remove Duplicates from Sorted List II
Medium

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr, prev = head, None
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                if not prev:
                    head = curr.next
                    curr = head
                else:
                    prev.next = curr.next
                    curr = prev.next
            else:
                prev = curr
                curr = curr.next
        return head
