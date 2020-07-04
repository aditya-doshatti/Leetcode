'''
1480. Running Sum of 1d Array
Easy

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

https://leetcode.com/problems/running-sum-of-1d-array/
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
        # retVal = []
        # sumVal = 0
        # for i in nums:
        #     sumVal += i
        #     retVal.append(sumVal)
        # return retVal
