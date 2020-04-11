'''
347. Top K Frequent Elements
Medium

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

https://leetcode.com/problems/top-k-frequent-elements/
'''
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        test = {}
        heap,retVal = [], []
        for num in nums:
            test[num] = test.get(num, 0) + 1
        for key in test:
            heapq.heappush(heap, (-test[key], key))
        for i in range(k):
            a,b = heapq.heappop(heap) 
            retVal.append(b)
        return retVal
