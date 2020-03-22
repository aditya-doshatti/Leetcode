'''
1046. Last Stone Weight
Easy

We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

https://leetcode.com/problems/last-stone-weight/
'''
# import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            a,b = stones[-1], stones[-2]
            stones = stones[:-2]
            if a-b:
                bisect.insort(stones, a-b)
        if len(stones) ==1:
            return stones[0]
        return 0
#         heapq._heapify_max(stones)
#         while len(stones) > 1:
#             #print(stones)
#             a, b = heapq._heappop_max(stones), heapq._heappop_max(stones)
#             if a > b:
#                 self._heappush_max(stones, a-b)
#             #print(stones)
#         if stones:
#             return stones[0]
#         else:
#             return 0
    
#     def _heappush_max(self, heap, item):
#         heap.append(item)
#         heapq._siftdown_max(heap, 0, len(heap)-1)
