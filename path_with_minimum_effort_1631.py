'''
1631. Path With Minimum Effort
Medium

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

https://leetcode.com/problems/path-with-minimum-effort/
'''
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(maxVal, x, y):
            visited.add((x, y)) 
            for dx, dy in dirs:
                if 0<=dx+x<m and 0<=dy+y<n and (dx+x, dy+y) not in visited:
                    if abs(heights[x][y] - heights[dx+x][dy+y]) <= maxVal:
                        dfs(maxVal, dx+x, dy+y)
        i, j = -1, max(max(heights, key=max))
        while i + 1 < j:
            mid = (i + j)//2
            visited = set()
            dfs(mid, 0, 0)
            if (m - 1, n - 1) in visited:
                j = mid
            else:
                i = mid
        return j
