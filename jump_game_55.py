'''
55. Jump Game
Medium

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

https://leetcode.com/problems/jump-game/
'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i, reachableFrom = len(nums)-1, len(nums)-1
        while i >=0:
            if i+nums[i] >= reachableFrom:
                reachableFrom = i
            i -=1
        return reachableFrom == 0
        # All test pass but too much time consuming
        # res, i = [0] * len(nums), len(nums)-1
        # if not nums or len(nums)==1:
        #     return True
        # while i >= 0 :
        #     if i + nums[i] + 1>= len(nums) or 1 in res[i:i+nums[i]+1]:
        #         res[i] = 1
        #     i -=1
        # #print(res)
        # return res[0]
        
