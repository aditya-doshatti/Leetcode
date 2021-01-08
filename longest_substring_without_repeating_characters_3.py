'''
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        i, retVal, dic = 0, 0, {}
        for index,c in enumerate(s):
            if c in dic and i <= dic[c]:
                i = dic[c]+1
            else:
                retVal = max(retVal, index-i+1)
            dic[c] = index
        return retVal
