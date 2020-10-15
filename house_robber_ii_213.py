'''
213. House Robber II
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

https://leetcode.com/problems/house-robber-ii/
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <4:
            return max(nums)
        prev, curr = 0, 0
        for num in nums[:-1]:
            prev, curr = curr, max(prev+num, curr)
        firstVal = curr
        prev, curr = 0, 0
        for num in nums[1:]:
            prev, curr = curr, max(prev+num, curr)
        secVal = curr
        return max(firstVal, secVal)
