'''
1512. Number of Good Pairs
Easy

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

https://leetcode.com/problems/number-of-good-pairs/
'''
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        retVal = 0
        for num in nums:
            if num in seen:
                retVal += seen[num]
            seen[num] = seen.get(num, 0) + 1 
        return retVal
