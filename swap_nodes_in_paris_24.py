'''
24. Swap Nodes in Pairs
Medium

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

https://leetcode.com/problems/swap-nodes-in-pairs/
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        retVal = head.next if head and head.next else head
        while head:
            temp, temp2 = None, None
            if head.next:
                temp = head.next
            if temp and temp.next:
                temp2 = temp.next
            if temp2 and temp2.next:
                head.next = temp2.next
            else:
                head.next = temp2
            if temp:
                temp.next = head
            head = temp2
        return retVal
