'''
611. Valid Triangle Number
Medium

Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

https://leetcode.com/problems/valid-triangle-number/
'''
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums, retVal, n = sorted(nums), 0, len(nums)
        for i in range(2, n):
            left, right = 0, i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    retVal += (right - left)
                    right -= 1
                else:
                    left += 1
        return retVal
