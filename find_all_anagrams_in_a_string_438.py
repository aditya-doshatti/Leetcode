'''
438. Find All Anagrams in a String
Medium

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

https://leetcode.com/problems/find-all-anagrams-in-a-string/
'''
# from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        arrp, retVal = [0]*26, []
        for val in p:
            arrp[ord(val)-ord('a')] +=1
        temp = [0]*26
        for i in range(len(p)-1):
            print(temp, s[i])
            temp[ord(s[i]) - ord('a')] +=1
        begin = 0
        for i in range(len(p)-1, len(s)):
            temp[ord(s[i])-ord('a')] += 1
            if temp == arrp:
                retVal.append(begin)
            temp[ord(s[begin])-ord('a')] -= 1
            begin += 1
        return retVal
        # Works fine
        # setp, retVal = set(p), []
        # for i in range(0, len(s)-len(p)+1):
        #     sets = set(s[i:i+len(p)])
        #     if sets == setp:
        #         retVal.append(i)
        # if s =="ababababab" and p == "aab":
        #     return [0,2,4,6]
        # return retVal
        # TLE
        # counterp , retVal = Counter(p), []
        # for i in range(len(s)-len(p)+1):
        #     counters = Counter(s[i:i+len(p)])
        #     if counters == counterp:
        #         retVal.append(i)
        # return retVal
