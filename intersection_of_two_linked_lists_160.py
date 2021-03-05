'''
160. Intersection of Two Linked Lists
Easy

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 
https://leetcode.com/problems/intersection-of-two-linked-lists/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        tempA = headA
        retVal = None
        while tempA:
            tempA.val *= -1
            tempA = tempA.next
        tempB = headB
        while tempB:
            if tempB.val < 0:
                retVal = tempB
                break
            tempB = tempB.next
        tempA = headA
        while tempA:
            tempA.val *= -1
            tempA = tempA.next
        return retVal
