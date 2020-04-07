'''
1347. Minimum Number of Steps to Make Two Strings Anagram
Medium

Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
'''
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        scounter, tcounter = {}, {}
        for i in string.ascii_lowercase:
            scounter[i] = s.count(i)
            tcounter[i] = t.count(i)
        retVal = 0 
        for key, values in scounter.items():
            if key in tcounter:
                if scounter[key] > tcounter[key]:
                    retVal += (scounter[key] - tcounter[key])
            else:
                retVal += scounter[key]
        return retVal
        # Not best time complexity
        # scounter, tcounter = {}, {}
        # for i in range(len(s)):
        #     scounter[s[i]] = scounter.get(s[i], 0) + 1
        #     tcounter[t[i]] = tcounter.get(t[i], 0) + 1
        # retVal = 0 
        # for key, values in scounter.items():
        #     if key in tcounter:
        #         if scounter[key] > tcounter[key]:
        #             retVal += (scounter[key] - tcounter[key])
        #     else:
        #         retVal += scounter[key]
        # return retVal
