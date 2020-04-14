'''
525. Contiguous Array
Medium

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

https://leetcode.com/problems/contiguous-array/
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0:-1}
        maxVal, curr = 0, 0
        for i in range(len(nums)):
            curr += 1 if nums[i] == 1 else -1
            if curr in dic:
                maxVal = max(maxVal, i - dic[curr])
            else:
                dic[curr] = i
        return maxVal
