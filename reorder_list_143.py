'''
143. Reorder List
Medium

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.

https://leetcode.com/problems/reorder-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        lst = []
        cur = head
        while(cur):
            lst.append(cur)
            cur = cur.next

        lst1 = lst[:len(lst)//2]
        lst2 = lst[len(lst)//2:]
        lst2.reverse()

        lst = []
        for i in range(len(lst2)):
            try:
                lst.append(lst1[i])
            except IndexError:
                pass
            lst.append(lst2[i])

        for i in range(len(lst)):
            try:
                lst[i].next = lst[i+1]
            except IndexError:
                lst[i].next = None
        
