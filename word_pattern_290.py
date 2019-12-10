'''
290. Word Pattern
Easy

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true

https://leetcode.com/problems/word-pattern/
'''
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        strs = str.split(" ")
        if len(strs) != len(pattern):
            return False
        dic1, dic2, i = {}, {}, 0
        while i < len(strs):
            val1 = dic1.get(pattern[i])
            val2 = dic2.get(strs[i])
            if val1:
                if strs[i] != val1 or not val2 or val2 != pattern[i]:
                    return False
            elif val2:
                return False
            else:
                dic1[pattern[i]] = strs[i]
                dic2[strs[i]] = pattern[i]                
            i+=1
        return True
