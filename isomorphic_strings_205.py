'''
205. Isomorphic Strings
Easy

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true

https://leetcode.com/problems/isomorphic-strings/
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic, visited = {}, set()
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] in visited:
                    return False
                dic[s[i]] = t[i]
            else:
                if t[i] != dic[s[i]]:
                    return False
            visited.add(t[i])
        return True
