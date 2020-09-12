'''
152. Maximum Product Subarray
Medium

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

https://leetcode.com/problems/maximum-product-subarray/
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod, min_prod, retVal = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            y = min(nums[i], max_prod*nums[i], min_prod*nums[i])            
            max_prod, min_prod = x, y
            retVal = max(max_prod, retVal)
        return retVal
