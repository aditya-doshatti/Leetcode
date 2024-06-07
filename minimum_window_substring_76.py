'''
76. Minimum Window Substring

Hard

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

https://leetcode.com/problems/minimum-window-substring/description/
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = Counter(t)
        l,r,minLen = 0, 0, float('inf')
        s_dict, prevr = defaultdict(int), -1
        retVal = ""
        while l <= r and r < len(s):
            if prevr != r:
                s_dict[s[r]] += 1
            prevr = r
            if self.compareDict(s_dict, t_dict):
                # print(l, r, s_dict, s[l:r+1])
                if minLen > r - l:
                    retVal = s[l:r + 1]
                    minLen = r - l
                s_dict[s[l]] -= 1
                l += 1
            else:
                r += 1
        return retVal

        
    def compareDict(self, s_dict, t_dict):
        for k,v in t_dict.items():
            # print( k in s_dict and s_dict[k] >= v, s_dict)
            if k in s_dict and s_dict[k] >= v:
                continue
            else:
                return False
        return True
