'''
63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

https://leetcode.com/problems/unique-paths-ii/
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0:
                    if j ==0:
                        if obstacleGrid[i][j] != 1:
                            obstacleGrid[i][j] = 1
                        else:
                            return 0
                    elif obstacleGrid[i][j] != 1:
                        obstacleGrid[i][j] = obstacleGrid[i][j-1]
                    else:
                        obstacleGrid[i][j] = 0
                else:
                    if j ==0:
                        if obstacleGrid[i][j] != 1:
                            obstacleGrid[i][j] = obstacleGrid[i-1][j]
                        else:
                            obstacleGrid[i][j] = 0
                    else:
                        if obstacleGrid[i][j] == 0:
                            obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
                        else:
                            obstacleGrid[i][j] = 0
        return obstacleGrid[-1][-1]
