'''
1171. Remove Zero Sum Consecutive Nodes from Linked List
Medium

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        curr = test = ListNode(0)
        test.next = head
        sumVal = 0
        dic = collections.OrderedDict()
        while curr:
            sumVal += curr.val
            node = dic.get(sumVal, curr)
            while sumVal in dic:
                dic.popitem()
            dic[sumVal] = node
            node.next = curr = curr.next
        return test.next
    # def removeZeroSumSublists(self, head: ListNode) -> ListNode:
    #     dic = collections.OrderedDict()
    #     dic[0] = None
    #     node,sumVal = head, 0
    #     while node:
    #         sumVal += node.val
    #         print(sumVal)
    #         while sumVal in dic:
    #             print("in")
    #             dic.popitem()
    #         if node.next:
    #             dic[sumVal] = node
    #         node = node.next
    #     retVal = None
    #     newHead = None
    #     print(dic)
    #     for i in dic:
    #         if dic[i] == None:
    #             continue
    #         elif newHead == None:
    #             newHead = ListNode(dic[i].val)
    #             retVal = newHead
    #         else:
    #             retVal.next = Node(dic[i].val)
    #             retVal = retVal.next
    #     return newHead
            
