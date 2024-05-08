'''
2816. Double a Number Represented as a Linked List

Medium

You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.

 

Example 1:


Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.

https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = self.reverse_node(head)
        current, carry, prev = newHead, 0, None
        while current:
            newVal = current.val*2
            current.val = (newVal % 10) + carry
            carry = newVal//10
            prev = current
            current = current.next
        if carry:
            newNode = ListNode(carry)
            prev.next = newNode
        return self.reverse_node(newHead)
        
    def reverse_node(self, node: ListNode) -> ListNode:
        previous, current = None, node
        while current:
            next_node = current.next
            current.next = previous
            previous, current = current, next_node
        return previous
        '''
        Runtime error 1205/1265
        number, node = "", head
        while node:
            number = number + str(node.val)
            node = node.next
        retNumber = str(int(number) * 2)
        # print(number, retNumber)
        if len(retNumber) > len(number):
            newNode = ListNode(int(retNumber[0]), head)
            head = newNode
        else:
            head.val = int(retNumber[0])
        new_ptr = head.next
        for i in range(1, len(retNumber)):
            # print(int(retNumber[i]), retNumber[i])
            new_ptr.val = int(retNumber[i])
            new_ptr = new_ptr.next
        return head
        '''
