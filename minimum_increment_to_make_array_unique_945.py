'''
945. Minimum Increment to Make Array Unique

Medium

You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].

https://leetcode.com/problems/minimum-increment-to-make-array-unique/description
'''
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        prev, retVal = nums[0], 0
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                retVal += (prev - nums[i] + 1)
                nums[i] = prev + 1
            prev = nums[i]
        return retVal
