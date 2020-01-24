'''
441. Arranging Coins
Easy

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

https://leetcode.com/problems/arranging-coins/
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Approach 1
        if n < 2:
            return n
        i = 1
        retVal = 0
        while retVal < n:
            retVal+=i
            i+=1
        if retVal == n:
            return i-1
        else:
            return i-2
        # Approach 2
        # while i < n+1:
        #     retVal +=i
        #     if retVal > n:
        #         return i-1
        #     i+=1
