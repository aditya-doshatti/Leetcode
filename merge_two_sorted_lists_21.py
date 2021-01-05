'''
21. Merge Two Sorted Lists
Easy

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

https://leetcode.com/problems/merge-two-sorted-lists/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and not l2:
            return l1
        elif l2 and not l1:
            return l2
        retVal = head = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            elif l2.val < l1.val:
                head.next = l2
                l2 = l2.next
            elif l1.val == l2.val:
                head.next = l1
                l1 = l1.next
                head = head.next
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 if l1 else l2
        return retVal.next
