'''
220. Contains Duplicate III
Medium

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

https://leetcode.com/problems/contains-duplicate-iii/
'''
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0: 
            return False
        d = {}
        w = t + 1
        for i in range(len(nums)):
            m = nums[i] // w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k: 
                del d[nums[i - k] // w]
        return False
        # 40/41 tests passed
        # i= 0
        # while i  < len(nums) or i < k:
        #     j = 1
        #     while j <= k and i+j < len(nums):
        #         if abs(nums[i]-nums[i+j]) <= t:
        #             return True
        #         j +=1
        #     i +=1
        # return False
