'''
738. Monotone Increasing Digits
Medium

Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9

https://leetcode.com/problems/monotone-increasing-digits/
'''
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        k = str(N)
        n = len(k) -2
        while n >= 0:
            if int(k[n]) > int(k[n+1]):
                k = str(int(k)-(int(k[n+1:])+1))
            n -= 1
        return int(k)
