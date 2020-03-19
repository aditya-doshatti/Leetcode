'''
942. DI String Match
Easy

Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
 

Example 1:

Input: "IDID"
Output: [0,4,1,3,2]

https://leetcode.com/problems/di-string-match/
'''
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        h, l, retVal = len(S), 0, []
        for i in S:
            if i == 'D':
                retVal.append(h)
                h -=1
            else:
                retVal.append(l)
                l +=1
        retVal.append(h)
        return retVal
