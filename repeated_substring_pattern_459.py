'''
459. Repeated Substring Pattern
Easy

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

https://leetcode.com/problems/repeated-substring-pattern/
'''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss = s + s
        ss= ss[1:-1]
        return s in ss
        # for i in range(1, len(s)//2+1):
        #     if len(s) % i == 0 and s[:i]*(len(s)//i) == s:
        #         return True
        # return False
