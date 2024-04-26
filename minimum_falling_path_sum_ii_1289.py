'''
1289. Minimum Falling Path Sum II
Hard
Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

 

Example 1:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation: 
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.
https://leetcode.com/problems/minimum-falling-path-sum-ii/description/
'''
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[n-1] = grid[n-1]
        for i in range(n-2, -1, -1):
            for j in range(len(grid[i])):
                dp[i][j] = min(min(dp[i+1][:j], default=float('inf')), min(dp[i+1][j+1:], default=float('inf'))) + grid[i][j]
        return min(dp[0])
