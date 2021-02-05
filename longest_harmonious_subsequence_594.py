'''
594. Longest Harmonious Subsequence
Easy

We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

https://leetcode.com/problems/longest-harmonious-subsequence/
'''
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = Counter(nums)
        retVal = 0
        for val in dic.keys():
            if val+1 in dic:
                retVal = max(retVal, dic[val+1] + dic[val])
        return retVal
