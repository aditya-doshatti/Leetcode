'''
482. License Key Formatting
Easy

You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

 

Example 1:

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.

https://leetcode.com/problems/license-key-formatting/
'''
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-','')
        first_len = len(s) % k
        other_part = s[first_len:]
        other_part = '-'.join(other_part[i:i+k] for i in range(0, len(other_part), k))
        if first_len != 0:
            s = s[0:first_len]
            if len(other_part) != 0:
                s += '-' + other_part
        else:
            s = other_part
        return s.upper()
