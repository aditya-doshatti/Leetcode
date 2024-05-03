'''
2435. Paths in Matrix Whose Sum Is Divisible by K
Attempted
Hard
Topics
Companies
Hint
You are given a 0-indexed m x n integer matrix grid and an integer k. You are currently at position (0, 0) and you want to reach position (m - 1, n - 1) moving only down or right.

Return the number of paths where the sum of the elements on the path is divisible by k. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:


Input: grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
Output: 2
Explanation: There are two paths where the sum of the elements on the path is divisible by k.
The first path highlighted in red has a sum of 5 + 2 + 4 + 5 + 2 = 18 which is divisible by 3.
The second path highlighted in blue has a sum of 5 + 3 + 0 + 5 + 2 = 15 which is divisible by 3.

https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/description/
'''
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        dp = [[[0] * k for _ in range(n)] for __ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                for remainder in range(k):
                    if i > 0:
                        dp[i][j][(remainder + grid[i][j] % k) % k] += dp[i-1][j][remainder]
                        dp[i][j][(remainder + grid[i][j] % k) % k] %= MOD
                    if j > 0:
                        dp[i][j][(remainder + grid[i][j] % k) % k] += dp[i][j-1][remainder]
                        dp[i][j][(remainder + grid[i][j] % k) % k] %= MOD
        print(dp)
        return dp[-1][-1][0]
        '''
        Memory Limit 73/88
        n, m = len(grid), len(grid[0])
        def get_sums(i, j, grid, k):
            top_val, left_val = 0, 0
            retVal = []
            if 0 <= i - 1 < len(grid):
                top_val = grid[i-1][j]
                if type(top_val) == tuple:
                    for val in top_val:
                        retVal.append((val + grid[i][j]) % k)
                else:
                    retVal.append((top_val + grid[i][j]) % k)
            if 0 <= j - 1 < len(grid[i]):
                left_val = grid[i][j-1]
                if type(left_val) == tuple:
                    for val in left_val:
                        retVal.append((val + grid[i][j]) % k)
                else:
                    retVal.append((left_val + grid[i][j]) % k)
            if len(retVal) == 0:
                retVal = [grid[i][j] % k]
            # print(retVal, i, j, left_val, top_val)          
            return tuple(retVal)
        for i in range(n):
            for j in range(m):
                grid[i][j] = get_sums(i, j, grid, k)
        # print(grid)
        final_tup = grid[-1][-1]
        count = 0
        for val in final_tup:
            if val % k == 0:
                count = count + 1
                count %= MOD
        return count
        '''
