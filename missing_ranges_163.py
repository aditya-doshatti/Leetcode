'''
163. Missing Ranges

Easy

You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.

Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]
Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]

https://leetcode.com/problems/missing-ranges/description/
'''
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        retVal = []
        for num in nums:
            if num > lower:
                retVal.append([lower, num - 1])
            lower = num + 1
        if lower <= upper:
            retVal.append([lower, upper])
        return retVal
        '''
        TLE 30/39
        retVal = []
        temp = []
        for i in range(lower, upper + 1):
            if i not in nums and len(temp) == 0:
                temp.append(i)
            elif i in nums and len(temp) == 1:
                temp.append(i-1)
                retVal.append(temp)
                temp = []
        if len(temp) == 1:
            temp.append(i)
            retVal.append(temp)
        return retVal
        '''
