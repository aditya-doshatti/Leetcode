'''
902. Numbers At Most N Given Digit Set
Hard

Given an array of digits, you can write numbers using each digits[i] as many times as we want.  For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than or equal to a given integer n.

 

Example 1:

Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation: 
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
'''
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        dp = [0] * len(s) + [1]
        for i in range(len(s)-1, -1 , -1):
            for digit in digits:
                if digit < s[i]:
                    dp[i] += len(digits) ** (len(s)-i-1)
                elif digit == s[i]:
                    dp[i] += dp[i+1]
        return dp[0] + sum(len(digits) ** i for i in range(1, len(s)))
