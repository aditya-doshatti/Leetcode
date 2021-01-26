'''
1437. Check If All 1's Are at Least Length K Places Away
Easy

Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

 

Example 1:



Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.

https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
'''
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) <= 0 or k <= 0:
            return True
        lastOne, firstOne = 0, True
        for i in range(len(nums)):
            if nums[i] == 1 and (firstOne or lastOne < i-k):
                firstOne = False
                lastOne = i
            elif nums[i] == 0:
                continue
            else:
                return False
        return True
