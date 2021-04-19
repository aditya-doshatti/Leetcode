'''
19. Remove Nth Node From End of List
Medium

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next and n == 1:
            return None
        temp, cnt = head, 0
        while cnt < n+1:
            if not temp:
                return head.next
            temp = temp.next
            cnt += 1
        newHead = head
        while temp:
            temp = temp.next
            newHead = newHead.next
        newHead.next = newHead.next.next
        return head
