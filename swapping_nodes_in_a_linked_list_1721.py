'''
1721. Swapping Nodes in a Linked List
Medium

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        fast = head
        for _ in range(k-1):
            fast = fast.next
        temp1 = fast
        fast = fast.next
        slow = head
        while fast:
            fast = fast.next
            slow = slow.next
        temp2 = slow        
        temp1.val, temp2.val = temp2.val, temp1.val
        return head
            
