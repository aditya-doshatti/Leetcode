'''
1221. Split a String in Balanced Strings
Easy

Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

https://leetcode.com/problems/split-a-string-in-balanced-strings/
'''
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        retVal, curr = 0, 0
        for char in s:
            if char == 'L':
                curr -= 1
            else:
                curr += 1
            if curr == 0:
                retVal +=1
        return retVal
