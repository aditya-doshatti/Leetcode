'''
258. Add Digits
Easy

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.

https://leetcode.com/problems/add-digits/
'''
class Solution:
    def addDigits(self, num: int) -> int:
        return num%9 if (num%9 or num == 0) else 9
