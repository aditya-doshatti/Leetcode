'''
2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

https://leetcode.com/problems/add-two-numbers/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        retVal = ListNode(-1, None)
        head = retVal
        while l2 and l1:
            newVal = l2.val + l1.val
            if carry:
                newVal += 1
                carry = 0
            if newVal > 9:
                carry = 1
                newVal = newVal % 10
            head.next = ListNode(newVal)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        temp = None
        if l1:
            head.next = l1
            temp = head.next
        if l2:
            head.next = l2
            temp = head.next
        if temp and carry:
            while temp and carry:
                temp.val = temp.val + 1
                if temp.val > 9:
                    temp.val = temp.val %10
                    carry = 1
                    head = temp
                    temp = temp.next
                else:
                    carry = 0
        if carry: 
            head.next = ListNode(1)
        return retVal.next
