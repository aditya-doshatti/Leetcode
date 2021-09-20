'''
115. Distinct Subsequences
Hard

Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit

https://leetcode.com/problems/distinct-subsequences/
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dic = {}
        def helper(i, j):
            M, N = len(s), len(t)
            if i == M or j == N or M - i < N - j:
                return int(j == len(t))
            if (i, j) in dic:
                return dic[i,j]
            retVal = helper(i + 1, j)
            if s[i] == t[j]:
                retVal += helper(i + 1, j + 1)
            dic[i, j] = retVal
            return retVal
        return helper(0,0)
