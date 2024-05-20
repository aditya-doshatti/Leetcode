'''
694. Number of Distinct Islands
Solved
Medium
Topics
Companies
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.


Example 1:

Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1

https://leetcode.com/problems/number-of-distinct-islands/description/
'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(start, shape, i, j):
            if i>=0 and j>=0 and i<len(grid) and j<len(grid[0]) and grid[i][j] == 1:
                shape.append((i-start[0], j-start[1]))
                grid[i][j] = 0
                for dx, dy in [(0,1), (1,0), (-1, 0), (0, -1)]:
                    dfs(start, shape, i + dx, j + dy)
            return shape

        unique_islands, islands = set(), 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island = tuple(dfs((i,j), [], i, j))
                    if island not in unique_islands:
                        unique_islands.add(island)
                        islands += 1
        return islands
        '''
        Accepted, but Time complexity not good
        islands, count = defaultdict(list), 0
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]):
                if grid[i][j] == 1:
                    islands[count].append((i, j))
                    grid[i][j] = 0
                    for dx, dy in [(0,1), (1,0), (-1, 0), (0, -1)]:
                        dfs(i + dx, j + dy)
            else:
                return
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    count += 1
        distinct_islands = set()
        for i in islands.keys():
            temp = set()
            sortedlist = sorted(islands[i], key=lambda x:x[0] + x[1])
            basex, basey = sortedlist[0][0], sortedlist[0][1]
            for i in range(1, len(sortedlist)):
                temp.add((sortedlist[i][0] - basex, sortedlist[i][1] - basey))
            distinct_islands.add(frozenset(temp))
        # print(distinct_islands)
        return len(distinct_islands)
        '''
