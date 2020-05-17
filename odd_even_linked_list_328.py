'''
328. Odd Even Linked List
Medium

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

https://leetcode.com/problems/odd-even-linked-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head
        even = firstEven = head.next
        while even and even.next:
            odd.next = even.next
            even.next = odd.next.next
            even, odd = even.next, odd.next
        odd.next = firstEven
        return head
