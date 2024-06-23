'''
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Medium

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.

https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
'''
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_heap,max_heap=[],[]
        i, j, maxVal, n = 0, 0, 0, len(nums)
        while j < n:
            heapq.heappush(min_heap, (nums[j],j))
            heapq.heappush(max_heap, (-nums[j],j))
            while -max_heap[0][0] - min_heap[0][0] > limit:
                i += 1
                while min_heap[0][1] < i: heapq.heappop(min_heap)
                while max_heap[0][1] < i: heapq.heappop(max_heap)
            maxVal = max(maxVal, j - i + 1)
            j += 1
        return maxVal
        '''
        TLE 56/61
        maxVal, minVal, i, j, retVal = float('-inf'), float('inf'), 0, 0, 0
        while i <= j and j < len(nums):
            maxVal = max(nums[i:j + 1])
            minVal = min(nums[i:j + 1])
            if abs(maxVal - minVal) <= limit:
                j += 1
            else:
                i += 1
            retVal = max(retVal, j - i)
        return retVal
        '''
