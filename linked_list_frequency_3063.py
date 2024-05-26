'''
3063. Linked List Frequency

Easy

Given the head of a linked list containing k distinct elements, return the head to a linked list of length k containing the 
frequency
 of each distinct element in the given linked list in any order.

Example 1:

Input: head = [1,1,2,1,2,3]

Output: [3,2,1]

Explanation: There are 3 distinct elements in the list. The frequency of 1 is 3, the frequency of 2 is 2 and the frequency of 3 is 1. Hence, we return 3 -> 2 -> 1.

Note that 1 -> 2 -> 3, 1 -> 3 -> 2, 2 -> 1 -> 3, 2 -> 3 -> 1, and 3 -> 1 -> 2 are also valid answers.

https://leetcode.com/problems/linked-list-frequency/description/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = defaultdict(int)
        while head:
            dic[head.val] += 1
            head = head.next
        returnHead = retVal = ListNode()
        for k,val in dic.items():
            newNode = ListNode(val)
            returnHead.next = newNode
            returnHead = newNode
        return retVal.next
