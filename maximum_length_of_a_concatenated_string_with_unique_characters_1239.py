'''
1239. Maximum Length of a Concatenated String with Unique Characters
Medium

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.

https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:    
        def dfs(arr: List[str], pos: int, res: str) -> int:
            if len(res) != len(set(res)):
                return 0
            retVal = len(res)
            for i in range(pos, len(arr)):
                retVal = max(retVal, dfs(arr, i + 1, res + arr[i]))
            return retVal
        return dfs(arr, 0, "")
