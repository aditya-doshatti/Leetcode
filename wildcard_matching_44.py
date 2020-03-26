'''
44. Wildcard Matching
Hard

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

https://leetcode.com/problems/wildcard-matching/
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lens, lenp = len(s), len(p)
        i, j = 0, 0
        star , temp = -1, -1
        while i < lens:
            if j < lenp and p[j] == '*':
                star = j
                temp = i
                j +=1
            elif j < lenp and (p[j] == '?' or p[j] == s[i]):
                j +=1
                i +=1
            elif star == -1:
                return False
            else:
                i = temp + 1
                j = star + 1
                temp += 1
        for a in p[j:]:
            if a != '*':
                return False
        return True
        # DP Solution           
        # dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
        # dp[0][0] = True
        # for j in range(1, len(p)+1):
        #     if p[j-1] != '*':
        #         break
        #     dp[0][j] = True
        # for i in range(1, len(s)+1):
        #     for j in range(1, len(p)+1):
        #         if p[j-1] == '?' or s[i-1] == p[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         elif p[j-1] == '*':
        #             dp[i][j] = dp[i-1][j-1] or dp[i-1][j] or dp[i][j-1]
        # return dp[-1][-1]
        
