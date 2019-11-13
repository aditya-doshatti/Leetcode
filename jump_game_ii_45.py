'''
45. Jump Game II
Hard

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

https://leetcode.com/problems/jump-game-ii/
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return 0
        i, j = 0, nums[0]
        retVal = 1
        while j < len(nums) -1:
            retVal += 1
            jump = max(a+nums[a] for a in range(i,j+1))
            i, j = j, jump
        return retVal
