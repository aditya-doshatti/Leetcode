'''
201. Bitwise AND of Numbers Range
Medium

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4

https://leetcode.com/problems/bitwise-and-of-numbers-range/
'''
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while(m<n):
            n = n &(n-1)
        return n
        # if m == n:
        #     return m
        # retVal,a,b = 1,m,n
        # while a > 1:
        #     a = a//2
        #     b = b//2
        #     retVal *= 2
        # if a==b and a==1:
        #     return retVal
        # else:
        #     return 0
