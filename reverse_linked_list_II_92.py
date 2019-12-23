'''
92. Reverse Linked List II
Medium

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

https://leetcode.com/problems/reverse-linked-list-ii/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        i = 0
        fptr, rptr = head, None
        while m > 1:
            rptr = fptr
            fptr = fptr.next
            m ,n = m-1, n-1
        pretop, preend = fptr, rptr
        while n:
            temp = fptr.next
            fptr.next = rptr
            rptr = fptr
            fptr = temp
            n-=1
        if preend:
            preend.next = rptr
        else:
            head = rptr
        pretop.next = fptr
        return head
