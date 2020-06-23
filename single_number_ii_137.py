'''
137. Single Number II
Medium

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3

https://leetcode.com/problems/single-number-ii/
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        appearedOnce, appearedTwice = 0, 0
        for num in nums:
            appearedOnce = (appearedOnce ^ num) & ~appearedTwice
            appearedTwice = (appearedTwice ^ num) & ~appearedOnce
        return appearedOnce
        
        # dict = {}
        # for val in nums:
        #     dict[val] = dict.get(val, 0) + 1
        # for k,v in dict.items():
        #     if v == 1:
        #         return k
