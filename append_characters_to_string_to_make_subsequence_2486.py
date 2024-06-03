'''
2486. Append Characters to String to Make Subsequence

Medium

You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.


Example 1:

Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("coachingding").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.

https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description
'''
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        retVal, curr = len(t), 0
        for i in range(len(s)):
            if s[i] == t[start]:
                curr += 1
                retVal -= 1
            if not retVal:
                return retVal
        return retVal 
