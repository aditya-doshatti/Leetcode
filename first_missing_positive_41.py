'''
41. First Missing Positive
Hard

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

https://leetcode.com/problems/first-missing-positive/
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] >= len(nums):
                nums[i] = 0
        for i in range(len(nums)):
            nums[nums[i]%len(nums)] += len(nums)
        for i in range(1,len(nums)):
            if nums[i]//len(nums) == 0:
                return i
        return len(nums)
