'''
188. Best Time to Buy and Sell Stock IV
Hard

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
'''
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2: 
            return 0
        if k >= len(prices) // 2:
            max_profit = 0
            for i in range(len(prices) - 1):
                max_profit += max(prices[i+1] - prices[i], 0)
            return max_profit
        dp = [[0 for _ in range(k+1)] for _ in range(len(prices))]
        for k1 in range(1, k+1):
            local_max = -prices[0]
            for i in range(1, len(prices)):
                dp[i][k1] = max(dp[i-1][k1], prices[i] + local_max)
                local_max = max(local_max, dp[i-1][k1-1] - prices[i])
        return dp[len(prices)-1][k]
        # n = len(prices)
        # if n < 2: 
        #     return 0
        # dp = [[0 for _ in range(k+1)] for _ in range(n)]
        # for k1 in range(1, k+1):
        #     for i in range(1, n):
        #         dp[i][k1] = dp[i-1][k1]
        #         for j in range(i):
        #             tmp = prices[i] - prices[j]
        #             tmp += dp[j][k1-1] if j > 0 and k1 - 1 > 0 else 0
        #             dp[i][k1] = max(dp[i][k1], tmp)
        # return dp[n-1][k]
