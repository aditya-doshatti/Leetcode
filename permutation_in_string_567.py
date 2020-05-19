'''
567. Permutation in String
Medium

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

https://leetcode.com/problems/permutation-in-string/
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        arrs1 = [0] * 26
        for val in s1:
            arrs1[ord(val) - ord('a')] += 1
        arrs2 = [0] * 26
        for i in range(len(s1)-1):
            arrs2[ord(s2[i])-ord('a')] += 1
        temp = 0
        for i in range(len(s1)-1, len(s2)):
            arrs2[ord(s2[i])-ord('a')] += 1
            if arrs1 == arrs2:
                return True
            arrs2[ord(s2[temp])-ord('a')] -= 1
            temp += 1
        return False
