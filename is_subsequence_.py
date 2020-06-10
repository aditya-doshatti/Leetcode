'''
Is Subsequence

Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3355/
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
         done = 0
        for i in range(len(s)):
            k = done
            for j in range(k, len(t)):
                if t[j] == s[i]:
                    done = j + 1
                    break
            if done == k:
                return False
        return True
        
        # i = 0
        # j = 0
        # while j < len(t) and i < len(s):
        #     if s[i]==t[j]:
        #         i+=1
        #     j+=1
        # return i==len(s)
