'''
322. Coin Change
Medium

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

https://leetcode.com/problems/coin-change/
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp, i, j = [[float('inf')]*(amount+1)]*len(coins), 0, 0
        while i < len(coins):
            j = 0 
            while j <= amount:
                if j == 0:
                    dp[i][j] = 0
                if j >= coins[i]:
                    dp[i][j] = min(dp[i][j-coins[i]]+1, dp[i-1][j])
                j+=1
            i+=1
        if dp[-1][-1] == float('inf'):
            return -1
        return dp[-1][-1]  
'''
Poor complexity, Code from video about dp can and should be optimzed
'''                 
