'''
485. Max Consecutive Ones
Easy
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

https://leetcode.com/problems/max-consecutive-ones/
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sumVal, maxVal = 0, float('-inf')
        for val in nums:
            if val == 1:
                sumVal += 1
            else:
                maxVal = max(maxVal, sumVal)
                sumVal = 0
        return max(maxVal, sumVal)
