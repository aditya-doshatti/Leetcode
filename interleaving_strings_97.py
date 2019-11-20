'''
97. Interleaving String
Hard

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

https://leetcode.com/problems/interleaving-string/
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # if len(s3) != len(s1) + len(s2):
        #     return False
        # else:
        #     cnt1, cnt2, cnt3, pv1, pv2 = 0, 0, 0, 0, 0
        #     for cnt3 in range(len(s3)):
        #         print (cnt1, cnt2, cnt3, pv1, pv2, s3[cnt3])
        #         if s3[cnt3] == s1[cnt1]:
        #             cnt1 +=1 
        #         else:
        #             cnt1 = pv1
        #         if s3[cnt3] == s2[cnt2]:
        #             cnt2 += 1
        #         else:
        #             cnt2 = pv2
        #         if cnt1 == pv1 and cnt2 == pv2:
        #             return False
        #     if cnt3 == len(s3):
        #         return True
        if len(s1) + len(s2) != len(s3):
            return False
        match = [[False for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        match[0][0] = True
        for i in range(1, len(s1) + 1):
            match[i][0] = match[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, len(s2) + 1):
            match[0][j] = match[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                match[i][j] = (match[i - 1][j] and s1[i - 1] == s3[i + j - 1]) \
                                       or (match[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return match[-1][-1]
