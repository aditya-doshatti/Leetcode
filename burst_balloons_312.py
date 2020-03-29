'''
312. Burst Balloons
Hard

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

https://leetcode.com/problems/burst-balloons/

Explanation: https://www.youtube.com/watch?v=IFNibRVgFBo
'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [i for i in nums if i > 0] + [1]
        numsLen = len(nums)
        dp = [[0]*numsLen for _ in range(numsLen)]

        for k in range(2, numsLen):
            for left in range(0, numsLen - k):
                right = left + k
                for i in range(left + 1,right):
                    dp[left][right] = max(dp[left][right],
                           nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][numsLen - 1]
        # Yet to understand this: (Faster solution)
        # if not nums:
        #     return 0
        # nums = [1] + [num for num in nums if num > 0] + [1]
        # n = len(nums)
        # dp = [[0] * n for _ in range(n)]
        # for width in range(2, n):
        #     for left in range(n - width):
        #         right = left + width
        #         border_product = nums[left] * nums[right]
        #         max_val = 0
        #         for mid in range(left + 1, right):
        #             val = dp[left][mid] + nums[mid] * border_product + dp[mid][right]
        #             if val > max_val:
        #                 max_val = val
        #         dp[left][right] = max_val
        # return dp[0][n - 1]
        # My Try
        # retVal = 1
        # while len(nums) > 3:
        #     minVal = min(nums[1:len(nums)])
        #     idx = nums.index(minVal)
        #     retVal = retVal + (nums[idx-1] * nums[idx] * nums[idx+1])
        #     nums.pop(idx)
        
