'''
1680. Concatenation of Consecutive Binary Numbers
Medium

Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

 

Example 1:

Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 

https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
'''
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binaryString = ""
        for i in range(1,n+1):
            binaryString += str(bin(i))[2:]
        decimal = int(binaryString, 2)
        return decimal % 1000000007
        # tillNow, retVal = 0, 0
        # while n > 0:
        #     k = n
        #     while k:
        #         val = k % 2
        #         if val:
        #             retVal += ((2**tillNow))
        #         tillNow += 1
        #         k //= 2
        #     n -=1
        # return retVal  % (10**9 + 7)
