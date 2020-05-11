'''
997. Find the Town Judge
Easy

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2

https://leetcode.com/problems/find-the-town-judge/
'''
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and not trust:
            return 1
        temp = defaultdict(int)
        for val in trust:
            temp[val[0]] -= 1
            temp[val[1]] += 1
        if temp:
            for key in temp:
                if temp[key] == N-1:
                    return key
        return -1
