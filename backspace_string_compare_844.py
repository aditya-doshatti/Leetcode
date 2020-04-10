'''
844. Backspace String Compare
Easy

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

https://leetcode.com/problems/backspace-string-compare/
'''
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        finals, finalt = '', ''
        bk = 0
        i = len(S) - 1
        while i >= 0:
            if S[i] == '#':
                bk += 1
            elif bk >0:
                bk -= 1
            else:
                finals = S[i] + finals
            i -= 1
        i = len(T) - 1
        bk = 0
        while i >= 0:
            if T[i] == '#':
                bk += 1
            elif bk >0:
                bk -= 1
            else:
                finalt = T[i] + finalt
            i -= 1
        return finals == finalt
