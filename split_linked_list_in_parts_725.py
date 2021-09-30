'''
725. Split Linked List in Parts
Medium

Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

 

Example 1:


Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

https://leetcode.com/problems/split-linked-list-in-parts/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if k == 1:
            return [head]
        curr = head
        N = 0
        while curr:
            N += 1
            curr = curr.next
        t_length = []
        length = N
        for i in range(k, 0, -1):
            t_length.append(math.ceil(length/i))
            length -= math.ceil(length/i)
        retVal = []
        cnt = 0
        lidx = 0
        prev = head
        curr = head
        next = head
        while curr:
            if cnt == t_length[lidx]-1:
                next = curr.next
                curr.next = None
                retVal.append(prev)
                prev = next
                curr = next
                cnt = 0
                lidx += 1
            else:
                curr = curr.next
                cnt += 1
        if prev:
            ret.append(prev)
        for i in range(lidx, len(t_length)):
            retVal.append(None)
        return retVal
        # tmp, lenVal = head, 0
        # while tmp:
        #     lenVal += 1
        #     tmp = tmp.next
        # modVal = lenVal % k
        # partVal = lenVal //k
        # retVal =[]
        # tmp, currVal,i = head, 1, 0
        # while tmp:
        #     print(currVal, partVal, modVal, i)
        #     if currVal == 1:
        #         retVal.append(tmp)
        #         tmp = tmp.next
        #         currVal += 1
        #     elif currVal < partVal:
        #         tmp = tmp.next
        #         currVal += 1
        #         continue
        #     elif i < modVal:
        #         tmp = tmp.next
        #         currVal += 1
        #         i += 1
        #         continue
        #     else:
        #         i += 1
        #         print("IN else")
        #         print(tmp.val)
        #         nexttmp = tmp.next
        #         tmp.next = None
        #         tmp = nexttmp
        #         currVal = 1
        # print(retVal)
        # return retVal
