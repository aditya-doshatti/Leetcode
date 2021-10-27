'''
504. Base 7
Easy

Given an integer num, return a string of its base 7 representation.

 

Example 1:

Input: num = 100
Output: "202"

https://leetcode.com/problems/base-7/
'''
class Solution:
    def convertToBase7(self, num: int) -> str:
        temp = num
        num = abs(num)
        result = num % 7
        power = 1
        while num//7 != 0:
            num = num//7
            result += ((num % 7) * 10**power)
            power += 1
        return str(result) if temp >= 0 else '-' + str(result)
