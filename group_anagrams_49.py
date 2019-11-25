'''
49. Group Anagrams
Medium

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

https://leetcode.com/problems/group-anagrams/
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ordDic = {}
        for word in strs:
            k = str(sorted(word))
            ordDic.setdefault(k, [])
            ordDic[k].append(word)
        retVal = []
        for val in ordDic:
            retVal.append(ordDic[val])
        return retVal
