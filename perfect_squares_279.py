'''
279. Perfect Squares
Medium

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

https://leetcode.com/problems/perfect-squares/
'''
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(1, n+1):
            minVal = i
            j, sq = 1, 1
            while sq <= i:
                minVal = min(minVal, 1 + dp[i - sq])
                j += 1
                sq = j * j
            dp[i] = minVal
        return dp[n]
