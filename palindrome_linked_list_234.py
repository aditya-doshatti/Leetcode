'''
234. Palindrome Linked List
Easy

Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true

https://leetcode.com/problems/palindrome-linked-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head , head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        def reverse(head):
            temp = None
            while head:
                a = head.next
                head.next = temp
                temp = head
                head = a
            return temp
        newHead = reverse(slow.next)
        while newHead:
            if head.val != newHead.val:
                return False
            head = head.next
            newHead = newHead.next
        return True
