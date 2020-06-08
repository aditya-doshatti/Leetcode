'''
518. Coin Change 2
Medium

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

https://leetcode.com/problems/coin-change-2/
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * (amount);    
        for coin in coins:
            for i in range(amount - coin + 1):
                if dp[i]:
                    dp[i + coin] += dp[i]
        return dp[amount]
        # if amount == 0:
        #     return 1
        # if not coins:
        #     return 0
        # coins.sort()
        # dp =[[0 for _ in range(amount+1)] for _ in range(len(coins))]
        # for i in range(len(coins)):
        #     for j in range(amount+1):
        #         if j == 0:
        #             dp[i][j] = 1
        #         elif i == 0:
        #             if j < coins[i]:
        #                 dp[i][j] = 0
        #             else:
        #                 dp[i][j] = dp[i][j - coins[i]]
        #         else:
        #             if j < coins[i]:
        #                 dp[i][j] = dp[i-1][j]
        #             else:
        #                 dp[i][j] = dp[i][j - coins[i]] + dp[i-1][j]
        # return dp[-1][-1]          
