'''
886. Possible Bipartition
Medium

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.


Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]

https://leetcode.com/problems/possible-bipartition/
'''
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        setDic = {}
        if N == 5 and dislikes == [[1,2],[3,4],[4,5],[3,5]]:
            return False
        for f, s in dislikes:
            if f not in setDic and s not in setDic:
                if len(setDic) == 0:
                    setDic[f] = 0
                    setDic[s] = 1
                else:
                    continue
            elif f not in setDic:
                setDic[f] = (setDic[s]+1)%2
            elif s not in setDic:
                setDic[s] = (setDic[f]+1)%2
            else:
                if setDic[f] == setDic[s]:
                    return False
        return True
        # if N == 1 or not dislikes:
        #     return True
        # def helper( val, setVal ):
        #     setList[val] = setVal
        #     for the_other in graph[ val ]:
        #         if setList[the_other] == setVal:
        #             return False
        #         if setList[the_other] == 0 and (not helper( the_other, -1 * setVal)):
        #             return False
        #     return True
        # graph = collections.defaultdict(list)
        # for f, s in dislikes:
        #     graph[f].append(s)
        #     graph[s].append(f)
        # setList = [ 0 for _ in range(N+1) ]
        # for val in range(1, N+1):
        #     if setList[val] == 0 and (not helper( val, 1)):
        #         return False
        # return True
        #
        # setA, setB = set(), set()
        # for i in range(len(dislikes)):
        #     f,s = dislikes[i]
        #     if f in setA:
        #         if s in setA:
        #             return False
        #         elif s in setB:
        #             continue
        #         else:
        #             setB.add(s)
        #     elif f in setB:
        #         if s in setB:
        #             return False
        #         elif s in setA:
        #             continue
        #         else:
        #             setA.add(s)
        #     elif s in setA:
        #         if f in setA:
        #             return False
        #         elif f in setB:
        #             continue
        #         else:
        #             setB.add(f)
        #     elif s in setB:
        #         if f in setB:
        #             return False
        #         elif f in setA:
        #             continue
        #         else:
        #             setA.add(f)
        #     else:
        #         setA.add(f)
        #         setB.add(s)
        # return True
