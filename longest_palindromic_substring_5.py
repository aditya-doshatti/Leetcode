'''
5. Longest Palindromic Substring
Medium

Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

https://leetcode.com/problems/longest-palindromic-substring/
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        retVal = s[0]
        for curr in range(len(s)):
            i, j = curr - 1, curr + 1
            while j < len(s) and s[j] == s[curr]:
                j += 1
            while (i > -1 and j < len(s)) and s[i] == s[j]:
                i -= 1
                j += 1
            retVal = s[i+1:j] if (j - i -1) > len(retVal) else retVal
        return retVal
