'''
628. Maximum Product of Three Numbers
Easy

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6

https://leetcode.com/problems/maximum-product-of-three-numbers/
'''
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1, min2, max1, max2, max3 = float('inf'), float('inf'), float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num
            if num >= max3:
                max1 = max2
                max2 = max3
                max3 = num
            elif num >= max2:
                max1 = max2
                max2 = num
            elif num >= max1:
                max1 = num
        print(min1, min2, max1, max2, max3)
        return max(min1*min2*max3, max1*max2*max3)
        # nums.sort()
        # negproduct = nums[0]*nums[1]*nums[-1]
        # posproduct = nums[-3]*nums[-2]*nums[-1]
        # return max(negproduct, posproduct)
