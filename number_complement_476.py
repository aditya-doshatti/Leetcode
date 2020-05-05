'''
476. Number Complement
Easy

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

https://leetcode.com/problems/number-complement/
'''
class Solution:
    def findComplement(self, num: int) -> int:
        # temp = 0
        # while 2**temp -1 < num:
        #     temp +=1
        return (2**(len(bin(num)) - 2) - 1) ^ num
