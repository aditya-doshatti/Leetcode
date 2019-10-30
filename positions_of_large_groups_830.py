'''
830. Positions of Large Groups

In a string S of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
The final answer should be in lexicographic order.

Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.

https://leetcode.com/problems/positions-of-large-groups/
'''

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        curr = 0
        i = 1
        retVal = []
        while i < len(S):
            if S[i-1] == S[i]:
                curr += 1
            else:
                if curr >=2:
                    retVal.append([i-1-curr,i-1])
                curr = 0
            i += 1
        if curr >=2:
            retVal.append([i-1-curr,i-1])
            curr = 0
        return retVal
