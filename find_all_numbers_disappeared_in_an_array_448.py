'''
448. Find All Numbers Disappeared in an Array
Easy

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        missing = []
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                missing.append(i)
        return missing
        # checkArr = [0] * len(nums)
        # for val in nums:
        #     checkArr[val-1] = 1
        # retVal = []
        # for i in range(len(nums)):
        #     if checkArr[i] == 0:
        #         retVal.append(i+1)
        # return retVal
