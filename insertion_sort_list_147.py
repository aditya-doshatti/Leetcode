'''
147. Insertion Sort List
Medium
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

https://leetcode.com/problems/insertion-sort-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        orig = head
        retVal, newList = None, None
        while orig:
            val = orig.val
            prev, newList = None, retVal
            while newList:
                if newList.val < val:
                    prev = newList
                    newList = newList.next
                else:
                    break
            if not prev:
                retVal = ListNode(val)
                if not newList:
                    newList = retVal
                else:
                    retVal.next = newList
            else:
                temp = prev.next
                prev.next = ListNode(val)
                prev.next.next = temp
            orig = orig.next
        return retVal          
