'''
1446. Consecutive Characters
Easy

Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

https://leetcode.com/problems/consecutive-characters/
'''
class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        curr, retVal = 1, 0
        prev = s[0]
        for i in range(1, len(s)):
            if s[i] == prev:
                curr += 1
            else:
                prev = s[i]
                retVal = max(curr, retVal)
                curr = 1
        return max(retVal, curr)
