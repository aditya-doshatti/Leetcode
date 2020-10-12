'''
316. Remove Duplicate Letters
Medium

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"

https://leetcode.com/problems/remove-duplicate-letters/
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        retVal = ''
        while s:
            print(list(map(s.rindex, set(s))))
            i = min(map(s.rindex, set(s)))
            c = min(s[:i+1])
            retVal += c
            s = s[s.index(c):].replace(c, '')
        return retVal
        
        # dic = Counter(s)
        # retVal, i = '', -1
        # while i < len(s)-2:
        #     i += 1
        #     if dic[s[i]] > 1:
        #         if s[i] > s[i+1]:
        #             continue
        #     retVal += s[i]
        # return retVal
