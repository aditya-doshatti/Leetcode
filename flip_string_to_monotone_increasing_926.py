'''
926. Flip String to Monotone Increasing
Medium

A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.

https://leetcode.com/problems/flip-string-to-monotone-increasing/
'''
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        retVal, change = 0, 0
        for i in range(len(s)):
            if s[i] == '1':
                change += 1
            else:
                retVal = min(retVal +1, change)
        return retVal
