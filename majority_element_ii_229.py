'''
229. Majority Element II
Medium

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]

https://leetcode.com/problems/majority-element-ii/
'''
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        n = len(nums)
        retVal = []
        for key in c:
            if c[key] > n/3:
                retVal.append(key)
        return retVal
