'''
2124. Check if All A's Appears Before All B's

Easy

Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

 

Example 1:

Input: s = "aaabbb"
Output: true
Explanation:
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.

https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/
'''
class Solution:
    def checkString(self, s: str) -> bool:
        bFound = False
        for char in s:
            if bFound and char == 'a':
                return False
            elif char == 'b':
                bFound = True
        return True
