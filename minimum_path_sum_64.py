'''
64. Minimum Path Sum
Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

https://leetcode.com/problems/minimum-path-sum/
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        temp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j== 0:
                    temp[i][j] = grid[i][j]
                elif i ==0:
                    temp[i][j] = temp[i][j-1] + grid[i][j]
                elif j == 0:
                    temp[i][j] = grid[i][j] + temp[i-1][j]
                else:
                    temp[i][j] = min(temp[i][j-1] + grid[i][j], temp[i-1][j] + grid[i][j])
        return temp[-1][-1]
