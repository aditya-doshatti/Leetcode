'''
23. Merge k Sorted Lists
Hard

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

https://leetcode.com/problems/merge-k-sorted-lists/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        arr= []
        for i in range(len(lists)):
            head = lists[i]
            while head:
                arr.append(head.val)
                head = head.next
        arr.sort()
        # print(arr)
        head = temp = ListNode()
        while arr:
            temp.next = ListNode(arr.pop(0))
            temp = temp.next
        return head.next
        # def mergeTwoLists(l1, l2):
        #     """
        #     :type l1: ListNode
        #     :type l2: ListNode
        #     :rtype: ListNode
        #     """
        #     curr = dummy = ListNode(0)
        #     while l1 and l2:
        #         if l1.val < l2.val:
        #             curr.next = l1
        #             l1 = l1.next
        #         else:
        #             curr.next = l2
        #             l2 = l2.next
        #         curr = curr.next
        #     curr.next = l1 or l2
        #     return dummy.next
        # if not lists:
        #     return None
        # i,j = 0 , len(lists)-1
        # while j >0:
        #     if i >= j:
        #         i = 0
        #     else:
        #         lists[i] = mergeTwoLists(lists[i], lists[j])
        #         i += 1
        #         j -= 1
        # return lists[0]
