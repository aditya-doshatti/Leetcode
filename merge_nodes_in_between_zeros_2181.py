'''
2181. Merge Nodes in Between Zeros

Medium

You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.
 
Example 1:


Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.

https://leetcode.com/problems/merge-nodes-in-between-zeros/description
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        retVal, sumVal = None, 0
        curr, newHead = head, ListNode(0, ListNode())
        while curr:
            if curr.val == 0 and sumVal != 0:
                newHead.next = ListNode(sumVal)
                while curr and curr.val == 0:
                    curr = curr.next
                if retVal == None:
                    retVal = newHead
                newHead = newHead.next
                sumVal = 0
            elif curr.val != 0:
                sumVal += curr.val
                curr = curr.next
            elif curr:
                curr = curr.next
        return retVal.next
