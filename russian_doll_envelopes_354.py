'''
354. Russian Doll Envelopes
Hard

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

 

Example 1:

Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

https://leetcode.com/problems/russian-doll-envelopes
'''
class Solution:
    def maxEnvelopes(self, A):
        A.sort(key = lambda x: (x[0], -x[1]))
        Y_val = [y for _,y in A]
        retVal = 0
        dp = []
        for y in Y_val:
            i = bisect.bisect_left(dp, y)
            if i == len(dp):
                dp.append(y)
            else:
                dp[i] = y
            if i == retVal:
                retVal += 1
        return retVal
