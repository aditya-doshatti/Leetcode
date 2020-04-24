'''
714. Best Time to Buy and Sell Stock with Transaction Fee
Medium

Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

https://www.youtube.com/watch?v=4gYjVurpvWY
'''
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy, sell = 0, -prices[0]
        for i in range(1, len(prices)):
            buy = max(buy, sell + prices[i] - fee)
            sell = max(sell, buy - prices[i])
        return buy
        
        # hold, sell = [0] * len(prices), [0] * len(prices)
        # hold[0], sell[0] = -prices[0], 0
        # for i in range(1, len(prices)):
        #     hold[i] = max(hold[i-1], sell[i-1] - prices[i])
        #     sell[i] = max(sell[i-1], hold[i-1] + prices[i] - fee)
        # return sell[-1]
