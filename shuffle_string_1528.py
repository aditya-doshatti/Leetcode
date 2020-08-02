'''
1528. Shuffle String
Easy

Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

 

Example 1:


Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

https://leetcode.com/problems/shuffle-string/
'''
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        retVal = [' '] * (len(s))
        for i, char in enumerate(s):
            retVal[indices[i]] = char
        return ''.join(retVal)
