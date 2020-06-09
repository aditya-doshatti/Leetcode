'''
231. Power of Two
Easy

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1

https://leetcode.com/problems/power-of-two/
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0 :
            return False
        binary = str(bin(n)[3:])
        return binary.count('1') == 0
        # if n == 1:
        #     return True
        # a = 2
        # while a <= n:
        #     if n == a:
        #         return True
        #     a*=2
        # return False
