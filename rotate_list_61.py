'''
61. Rotate List
Medium

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

https://leetcode.com/problems/rotate-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        temp, counter, attachPoint = head, 1, None
        if not head or k == 0:
            return head
        while temp.next != None:
            temp = temp.next
            counter += 1
            if attachPoint:
                attachPoint = attachPoint.next
            if counter == k+1:
                attachPoint = head
        if not attachPoint:
            k = k % counter
            counter = 0
            temp = head
            while temp.next != None:
                temp = temp.next
                counter += 1
                if attachPoint:
                    attachPoint = attachPoint.next
                if counter == k:
                    attachPoint = head
        if not attachPoint:
            return head
        newHead = attachPoint.next
        temp.next = head
        attachPoint.next = None
        return newHead             
