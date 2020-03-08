'''
203. Remove Linked List Elements
Easy

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

https://leetcode.com/problems/remove-linked-list-elements/
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        if head.val == val:
            while head.next and head.val == val:
                head = head.next
        if head.val == val:
            return None
        curr, prev = head, head
        while curr and curr.next:
            if curr.val == val:
                while curr.next and curr.next.val == val:
                    curr = curr.next
                prev.next = curr.next
            prev = curr
            curr = curr.next
        if curr and curr.val == val:
            prev.next = None
        return head
        
