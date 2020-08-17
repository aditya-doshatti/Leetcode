'''
123. Best Time to Buy and Sell Stock III
Hard

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: 
            return 0
        n, k = len(prices), 2
        B = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]
        if k > len(prices)//2: 
            return sum(x for x in B if x > 0)
        dp = [[0]*(k+1) for _ in range(n-1)] 
        retVal = [[0]*(k+1) for _ in range(n-1)] 
        dp[0][1], retVal[0][1] = B[0], B[0]
        for i in range(1, n-1):
            for j in range(1, k+1):
                dp[i][j] = max(retVal[i-1][j-1], dp[i-1][j]) + B[i]
                retVal[i][j] = max(dp[i][j], retVal[i-1][j])
        return max(retVal[-1])
