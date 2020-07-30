'''
309. Best Time to Buy and Sell Stock with Cooldown
Medium

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        prev_sell = 0
        curr_sell = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            temp = curr_sell
            curr_sell = max(curr_sell, hold + prices[i])
            hold = max(hold, (prev_sell if i >= 2 else 0) - prices[i])
            prev_sell = temp
        return curr_sell
