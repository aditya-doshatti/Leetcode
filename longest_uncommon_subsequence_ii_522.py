'''
522. Longest Uncommon Subsequence II
Medium
Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.

A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).
 

Example 1:

Input: strs = ["aba","cdc","eae"]
Output: 3

https://leetcode.com/problems/longest-uncommon-subsequence-ii/
'''
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        dic = collections.Counter(strs)
        def isSub(s1, s2):
            it = iter(s2)
            return all(i in it for i in s1)
        
        for s1 in sorted([s for s in dic if dic[s] == 1], key=len, reverse=True):
            if sum(isSub(s1, s2) for s2 in strs) == 1:
                return len(s1)
        return -1
