'''
2487. Remove Nodes From Linked List

Medium

You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.

https://leetcode.com/problems/remove-nodes-from-linked-list/description/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head)
            head = head.next
        maxVal = 0
        currHead = None
        while stack:
            node = stack.pop()
            if node.val >= maxVal:
                maxVal = node.val
                if currHead:
                    tmp = currHead
                    currHead = node
                    currHead.next = tmp
                else:
                    currHead = node
        return currHead
        '''
        Before reading hints
        pointer, curr = head, head
        minVal, maxVal = head.val, head.val
        while pointer:
            print(pointer.val)
            # print("inside else")
            if minVal < pointer.val:
                print("inside case1")
                if maxVal < pointer.val:
                    print("inside case1.1")
                    head = pointer
                    curr = pointer
                    minVal = pointer.val
                    maxVal = pointer.val
                else:
                    print("inside case1.2")
                    curr.next = pointer
                    curr = curr.next
                    minVal = pointer.val
            elif minVal > pointer.val:
                print("inside case2")
                minVal = pointer.val
            elif maxVal > pointer.val:
                print("inside case3")
                maxVal = pointer.val
            pointer = pointer.next
            # print(minVal, maxVal, curr.val, head.val, pointer)
        return head
        '''
