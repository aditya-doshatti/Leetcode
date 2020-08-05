'''
342. Power of Four
Easy

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true

https://leetcode.com/problems/power-of-four/
'''
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        binary = bin(num)[2:]
        if len(binary)%2:
            if binary[0] == '1' and all(i=='0' for i in binary[1:]):
                return True
        return False
